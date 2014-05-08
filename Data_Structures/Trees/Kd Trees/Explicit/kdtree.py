from node import Node
from queue import Queue
from stack import Stack
from pq import PriorityQueue
import os


class KDTree(object):
    ##PRECONDITION: Nodes cannot have the same x, y, r, g, or b values.

    def __init__(self, nodes, dim):
        '''(KDTree, list of Nodes, int) -> NoneType
        Make a new KDTree.'''

        self.dim = dim
        self.root = self.build_tree(nodes)
        self.num = len(nodes)


    def __repr__(self):
        '''(KDTree) -> str.'''

        return str(self.root)


    def build_tree(self, nodes=[], depth=0):
        '''(KDTree, list of Nodes, int) -> Node
        Return the root Node that represents KDTree with
        respect to its nodes.'''

        if nodes:
            axis = depth % self.dim

            nodes = sorted(nodes, key=lambda node: node.p[axis])
            med = len(nodes) // 2

            node = nodes[med]
            node.left = self.build_tree(nodes[:med], depth + 1)
            node.right = self.build_tree(nodes[med + 1:], depth + 1)
            return node


    def sort(self):
        '''(KDTree) -> list of Nodes
        Return a sorted list of Nodes.'''

        return self.inorder()


    def print_tree(self):
        '''(KDTree) -> NoneType
        Print KDTree.'''

        self._print_tree(self.root, '')


    def _print_tree(self, root, indent, i=1):
        '''(KDTree, Node, str, int) -> NoneType
        Print the tree rooted at root. Print indent (which consists only of
        whitespace) before the root value; indent more for the subtrees
        so that it looks nice.'''

        if root:
            self._print_tree(root.right, indent + '        |' + str(i) + "| ", \
            i + 1)
            print indent + str(root)
            self._print_tree(root.left, indent + '        |' + str(i) + "| ", \
            i + 1)


    def ret_tree(self):
        '''(KDTree) -> list of str
        Return a list of str that represent KDTree.'''

        return self._ret_tree(self.root, '', [])


    def _ret_tree(self, root, indent, tree=[], i=1):
        '''(KDTree, Node, str, list of str, int) -> list of str
        Return the string representation of KDTree from depth
        i - 1.'''

        if root:
            self._ret_tree(root.right, indent + '        |' + str(i) + "| ", \
            tree, i + 1)
            tree.append(indent + str(root) + '\n')
            self._ret_tree(root.left, indent + '        |' + str(i) + "| ", \
            tree, i + 1)
        return tree


    def write_tree(self):
        '''(KDTree) -> NoneType
        Write the string representation of KDTree to 'tree.txt'
        in the same directory.'''

        if os.path.exists('tree.txt'):
            os.remove('tree.txt')
        FILE = open('tree.txt', 'w')
        FILE.writelines(self.ret_tree())
        FILE.close()


    def flat(self):
        '''(KDTree) -> list of Nodes
        Return a flattened list of nodes that represents KDTree.'''

        #Refer to Node.flat()
        return self.root.flat()


    def insert(self, node):
        '''(KDTree, Node) -> Node
        Return the root Node of the resulting KDTree from inserting Node
        node.'''

        self.num += 1
        return self._insert(self.root, node)


    def _insert(self, root, node, depth=0):
        '''(KDTree, Node, Node, int) -> Node.'''

        if not root:
            return node

        axis = depth % self.dim
        if node.p[axis] < root.p[axis]:
            root.left = self._insert(root.left, node, depth + 1)
        elif node.p[axis] > root.p[axis]:
            root.right = self._insert(root.right, node, depth + 1)
        return root


    def remove(self, node):
        '''(KDTree, Node) -> Node
        Return the root Node of the resulting KDTree from removing Node
        node.'''

        if self.contains(node):
            self.num -= 1
        #Unchanged tree if node not in tree.
        return self._remove(self.root, node)


    def _remove(self, root, node, depth=0):
        '''(KDTree, Node, Node, int) -> Node.'''

        if not root:
            return None

        axis = depth % self.dim
        if node.p[axis] == root.p[axis]:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                root.p = self.largest(root.left).p
                root.left = self._remove(root.left, root, depth + 1)
                return root
        elif node.p[axis] < root.p[axis]:
            root.left = self._remove(root.left, node, depth + 1)
        else:
            root.right = self._remove(root.right, node, depth + 1)
        return root


    def largest(self, root):
        '''(KDTree, Node) -> Node
        Return the largest Node in the tree rooted at root.
        Precondition: root is not None
        '''

        if not root.right:
            return root
        return self.largest(root.right)


    def smallest(self, root):
        '''(KDTree, Node) -> Node
        Return the smallest Node in the tree rooted at root.
        Precondition: root is not None
        '''

        if not root.left:
            return root
        return self.smallest(root.left)


    def contains(self, node):
        '''(KDTree, Node) -> bool
        Return whether KDTree contains Node node.'''

        return self._contains(self.root, node)


    def _contains(self, root, node, depth=0):
        '''(KDTree, Node, Node, int) -> bool.'''

        if not root:
            return False

        axis = depth % self.dim
        if node.p[axis] < root.p[axis]:
            return self._contains(root.left, node, depth + 1)
        elif node.p[axis] > root.p[axis]:
            return self._contains(root.right, node, depth + 1)
        return True


    def find(self, node):
        '''(KDTree, Node) -> Node
        Return the Node in KDTree that resembles Node node.'''

        return self._find(self.root, node)


    def _find(self, root, node, depth=0):
        '''(KDTree, Node, Node, int) -> Node.'''

        if root:
            axis = depth % self.dim
            if node.p[axis] < root.p[axis]:
                return self._find(root.left, node, depth + 1)
            elif node.p[axis] > root.p[axis]:
                return self._find(root.right, node, depth + 1)
            return root


    def parent(self, node):
        '''(KDTree, Node) -> Node
        Return the parent Node of Node node.'''

        return self._parent(self.root, node)


    def _parent(self, root, node, depth=0):
        '''(KDTree, Node, Node, int).'''

        if root:
            if root.left:
                if root.left.p == node.p:
                    return root
            elif root.right:
                if root.right.p == node.p:
                    return root

            axis = depth % self.dim
            if node.p[axis] < root.p[axis]:
                return self._parent(root.left, node, depth + 1)
            elif node.p[axis] > root.p[axis]:
                return self._parent(root.right, node, depth + 1)
            else:
                return root


    def children(self, node):
        '''(KDTree, Node) -> list of Nodes
        Return a list of the children of node Node.'''

        #Return the children iff node is in KDTree.
        node = self.find(self.root, node)
        if node:
            return node.children()
        return []


    def left(self, root, nodes=[]):
        '''(KDTree, Node, list of Nodes) -> list of Nodes
        Return a list of all the left children in KDTree rooted at Node root.'''

        if root:
            if root.left and root.right:
                return self.left(root.left, nodes) + \
                       self.left(root.right, nodes) + [root.left]
            elif root.left:
                return self.left(root.left, nodes) + [root.left]
            elif root.right:
                return self.left(root.right, nodes)
            return nodes
        return nodes


    def right(self, root, nodes=[]):
        '''(KDTree, Node, list of Nodes) -> list of Nodes
        Return a list of all the right children in KDTree rooted at Node
        root.'''

        if root:
            if root.left and root.right:
                return self.right(root.left, nodes) + \
                       self.right(root.right, nodes) + [root.right]
            elif root.left:
                return self.right(root.left, nodes)
            elif root.right:
                return self.right(root.right, nodes) + [root.right]
            return nodes
        return nodes


    def is_leaf(self, node):
        '''(KDTree, Node) -> bool
        Return whether Node node is a leaf. Should only be used
        on a Node in KDTree.'''

        if node:
            if not(node.left or node.right):
                return True
        return False


    def NNSearch(self, node):
        '''(KDTree, Node) -> Node
        Return the nearest neighbour Node of Node node.'''

        return self._NNSearch(self.root, node)


    def _NNSearch(self, root, node, depth=0, best=float('inf'), nbest=None):
        '''(KDTree, Node, Node, int, int, Node) -> Node.'''

        if not(node or root):
            return nbest

        axis = depth % self.dim
        dist = node.sqdist(root)
        #Avoid duplicating nodes with last clause
        if (dist < best): #and not(node.p == root.p) and \
           #self.get_depth(node) > self.get_depth(root):
            best = dist
            nbest = root
        diff = node.p[axis] - root.p[axis]
        (close, away) = (root.left, root.right) if diff <= 0 else \
            (root.right, root.left)
        if close:
            return self._NNSearch(close, node, depth + 1, best, nbest)
        return nbest


    def max_depth(self, root, depth=0):
        '''(KDTree, Node, int) -> int
        Return the maximum depth from the KDTree rooted at Node root.'''

        if not(root):
            return depth - 1

        return max(self.max_depth(root.left, depth + 1), \
                   self.max_depth(root.right, depth + 1))


    def min_depth(self, root, depth=0):
        '''(KDTree, Node, int) -> int
        Return the minimum depth from the KDTree rooted at Node root.'''

        if not(root):
            return depth - 1

        return min(self.min_depth(root.left, depth + 1), \
                   self.min_depth(root.right, depth + 1))


    def is_full(self):
        '''(KDTree) -> bool
        Return whether the KDTree is full.'''

        return self.max_depth(self.root) == self.min_depth(self.root)


    def at_depth(self, stop_depth):
        '''(KDTree, int) -> list of Nodes
        Return a list of nodes of depth int stop_depth.'''

        return self._at_depth(self.root, stop_depth)


    def _at_depth(self, root, stop_depth, nodes=[], depth=0):
        '''(KDTree, Node, int, list of Nodes, int) -> list of Nodes.'''

        if not (root):
            return nodes

        if depth == stop_depth:
            return nodes + [root]
        return self._at_depth(root.left, stop_depth, nodes, depth + 1) + \
               self._at_depth(root.right, stop_depth, nodes, depth + 1)


    def get_depth(self, node):
        '''(KDTree, Node) -> int
        Return the depth of Node node in KDTree.
        If node is not in KDTree, return 0.'''

        return self._get_depth(self.root, node)


    def _get_depth(self, root, node, depth=0):
        '''(KDTree, Node, Node, int) -> int.'''

        if root:
            axis = depth % self.dim
            if node.p[axis] < root.p[axis]:
                return self._get_depth(root.left, node, depth + 1)
            elif node.p[axis] > root.p[axis]:
                return self._get_depth(root.right, node, depth + 1)
            else:
                return depth
        return 0


    def siblings(self, node):
        '''(KDTree, Node) -> list of Nodes
        Return the siblings of Node node.'''

        nodes = []
        node = self.find(node)
        if node:
            depth = self.get_depth(node)
            #if node is self.root or not in tree
            #no siblings are returned
            if depth:
                nodes = self.at_depth(depth)
                nodes.remove(node)
            return nodes
        return nodes


    def path(self, node):
        '''(KDTree, Node) -> list of Nodes
        Return a list of Nodes that represent the successive
        nodes from the root of KDTree to Node node.'''

        if self.contains(node):
            #If code is executed without checking if tree contains
            #Node node, function will return probable path to node
            #as if it were to be inserted.
            return self._path(self.root, node, [])
        return []


    def _path(self, root, node, nodes=[], depth=0):
        '''(KDTree, Node, Node, list of Nodes, int) -> list of Nodes.'''

        if root:
            nodes.append(root)
            axis = depth % self.dim
            if node.p[axis] < root.p[axis]:
                return self._path(root.left, node, nodes, depth + 1)
            elif node.p[axis] > root.p[axis]:
                return self._path(root.right, node, nodes, depth + 1)
        return nodes + [node] if nodes[-1].p != node.p else nodes


    def leaves(self):
        '''(KDTree) -> list of Nodes
        Return the leaves of KDTree.'''

        return self._leaves(self.root, [])


    def _leaves(self, root, nodes=[]):
        '''(KDTree, Node, list of Nodes) -> list of Nodes.'''

        if not(root.left or root.right):
            nodes.append(root)

        if root.left:
            self._leaves(root.left, nodes)
        if root.right:
            self._leaves(root.right, nodes)
        return nodes


    def is_internal(self, node):
        '''(KDTree, Node) -> bool
        Return whether Node node is an internal Node.'''

        return not(self.is_leaf(node))


    def inorder(self):
        '''(KDTree) -> list of Nodes
        Return the inorder traversal of KDTree.'''

        return self._inorder(self.root, [])


    def _inorder(self, root, order=[]):
        '''(KDTree, Node, list of Nodes) -> list of Nodes.'''

        #Note: tree.flat().sort() is in O(n ** 3 * log(n))
        #assuming that the default sort is in O(n) but
        #tree.sort() is in O(n ** 2 * log(n))
        if not root:
            return order

        if root.left:
            if root.right:
                return self._inorder(root.left, order) + \
                [root] + self._inorder(root.right, order)
            return self._inorder(root.left, order) + [root]
        if root.right:
            return [root] + self._inorder(root.right, order)
        return order + [root]


    def postorder(self):
        '''(KDTree) -> list of Nodes
        Return the postorder traversal of KDTree.'''

        return self._postorder(self.root, [])


    def _postorder(self, root, order=[]):
        '''(KDTree, Node, list of Nodes) -> list of Nodes.'''

        if not root:
            return order

        if root.left:
            if root.right:
                return self._postorder(root.left, order) + \
                self._postorder(root.right, order) + [root]
            return self._postorder(root.left, order) + [root]
        if root.right:
            return self._postorder(root.right, order) + [root]
        return order + [root]


    def preorder(self):
        '''(KDTree) -> list of Nodes
        Return the preorder traversal of KDTree.'''

        return self._preorder(self.root, [])


    def _preorder(self, root, order=[]):
        '''(KDTree, Node, list of Nodes) -> list of Nodes.'''

        if not root:
            return order

        if root.left:
            if root.right:
                return [root] + self._preorder(root.left, order) + \
                self._preorder(root.right, order)
            return [root] + self._preorder(root.left, order)
        if root.right:
            return [root] + self._preorder(root.right, order)
        return [root] + order


    def level_order(self):
        '''(KDTree) -> list of Nodes
        Return the level order of KDTree.'''

        order = []
        if self.root:
            Q = Queue()
            Q.enqueue(self.root)
            while not Q.is_empty():
                node = Q.dequeue()
                order.append(node)
                if node.left:
                    Q.enqueue(node.left)
                if node.right:
                    Q.enqueue(node.right)
        return order


    def depth_order(self):
        '''(KDTree) -> list of Nodes
        Return the depth order of KDTree.'''

        order = []
        if self.root:
            st = Stack()
            st.push(self.root)
            while not st.is_empty():
                node = st.pop()
                order.append(node)
                if node.left:
                    st.push(node.left)
                if node.right:
                    st.push(node.right)
        return order


    def mod(self, expr):
        '''(KDTree, str) -> NoneType
        Recursively modify Node and all its children to store
        the evaluation of str expr in their cargo.'''

        #root follows a recursive definition
        #self points to tree still
        return self._mod(expr, self.root, 0)


    def _mod(self, expr, root, depth=0):
        '''(KDTree, str, root, int) -> NoneType.'''

        if root:
            root.cargo = eval(expr)
            self._mod(expr, root.left, depth + 1)
            self._mod(expr, root.right, depth + 1)


    def index(self, node):
        '''(KDTree, Node) -> int
        Return the index of the nearest Node in KDTree. of Node node.'''

        return self.inorder().index(self.NNSearch(node))


    def at_index(self, index):
        '''(KDTree, int) -> Node
        Return the Node at int index.'''

        if (-(self.num + 1) <= index <= self.num):
            return self.inorder()[index]


    def BBFSearch(self, node):
        '''(KDTree, Node) -> Node
        Return the approximative nearest neighbour of Node node.
        
        TODO: Finish this.'''

        pass


    def _BBFSearch(self, root, node, depth=0, best=float('inf'), nbest=None):
        '''(KDTree, Node, Node, int, int, Node) -> Node.
        TODO: Complete this.'''

        PQ = PriorityQueue()
        PQ.enqueue(root, 0)
        while not(PQ.is_empty()):
            root = PQ.dequeue()
            dist = root.sqdist(node)
            if dist >= best:
                break
            while not(self.is_leaf(root)):
                pass


    def lower_bound(self, root, cut_dim, lowest=float('inf')):
        '''(KDTree, Node, int, int) -> int
        Return the lower bound of Node root.'''

        if not root:
            return lowest

        lowest = min(lowest, root.p[cut_dim])
        lowest = self.lower_bound(root.left, cut_dim, lowest)
        lowest = self.lower_bound(root.right, cut_dim, lowest)
        return lowest


    def upper_bound(self, root, cut_dim, highest=float('inf')):
        '''(KDTree, Node, int, int) -> int
        Return the upper bound of Node root.'''

        if not root:
            return highest

        highest = max(highest, root.p[cut_dim])
        highest = self.lower_bound(root.left, cut_dim, highest)
        highest = self.lower_bound(root.right, cut_dim, highest)
        return highest


if __name__ == '__main__':
    nodes = []
    num = int(raw_input("How many nodes? "))
    if num >= 0:
        for i in range(num):
            nodes.append(Node(i, 2*i, 3*i, 4*i, 5*i))


    tree = KDTree(nodes, 5)
    print "root: " + str(tree)
    #print tree.flat(tree.build_tree(nodes))
    big = tree.largest(tree.root)
    small = tree.smallest(tree.root)
    max_dist = big.sqdist(small)
    print "maximum distance: " + str(max_dist) + "\n"
    #tree.print_tree()

    #tree.root.mod('root.sqdist(Node(x, y))')
    #stores distance from query in Node.cargo
