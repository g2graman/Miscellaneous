class Node(object):
	def __init__(self, key, left=None, right=None):
		assert(isinstance(key, int))
		assert(isinstance(left, int) or left==None)
		assert(isinstance(right, int) or right==None)

		self.parent = self
		self.key = key
		self.left = left
		self.right = right

		if(self.left):
			assert(self.left.key < self.key)
			self.left.parent = self

		if(self.right):
			assert(self.right.key > self.key)
			self.right.parent = self


	def find(self, val):
		if(val > self.key):
			if (self.right):
				return self.right.find(val)
			else:
				return self
		elif(val < self.key):
			if (self.left):
				return self.left.find(val)
			else:
				return self
		return self


	def find_parent(self, val):
		return self.find(val).parent


	def contains(self, val):
		return self.find(val).key == val


	def insert(self, val):
		f_node = self.find(val)
		if(f_node and f_node.key != val):
			if(val > f_node.key):
				f_node.right = Node(val)
				f_node.right.parent = f_node
			else:
				f_node.left = Node(val)
				f_node.left.parent = f_node


	def print_tree(self):
		'''(Node) -> NoneType
		Print the BST rooted at self.'''

		self._print_tree(self, '')


	def _print_tree(self, root, indent, i=1):
		'''(Node, Node, str, int) -> NoneType
		Print the tree rooted at root. Print indent (which consists only of
		whitespace) before the root value; indent more for the subtrees
		so that it looks nice.'''

		if root:
			self._print_tree(root.right, indent + '        |' + str(i) + "| ", \
			i + 1)
			print indent + str(root.key)
			self._print_tree(root.left, indent + '        |' + str(i) + "| ", \
			i + 1)


	def remove(self, val):
		assert(self.key != val)
		self._remove(self, val)

	def _remove(self, root, val):
		p_node = self.find_parent(val)
		if(val > p_node.key):
			r_node = p_node.right
		elif(val < p_node.key):
			r_node = p_node.left
		else:
			r_node = p_node

		if(r_node):
			if(r_node.left):
				if(r_node.right):
					s = self.successor(r_node)
					s.left = r_node.left
					s.parent = p_node
					s.left.parent = s
					p_node.right = s
				else:
					r_node.left.parent = p_node
					p_node.left = r_node.left
			else:
				if(r_node.right):
					r_node.right.parent = p_node
					p_node.right = r_node.right


	def successor(self, root):
		current = root
		assert(current != None)
		if(root.right):
			current = root.right
			while(current.left):
				current = current.left
			return current
		#return None 	--> by default
