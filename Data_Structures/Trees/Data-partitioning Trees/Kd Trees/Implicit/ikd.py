class ImplicitKDTree(object):
	'''An Implicit min kd-tree. To turn into max kd-tree,
	change self._bubble_up(list, int), self._bubble_down(int),
	and self._is_smaller(int).'''


	def __init__(self, nodes, dim):
		'''(ImplicitKDTree, list of tuples, int) -> NoneType.'''

		self.nodes = nodes
		self.num = len(nodes)
		self.dim = dim
		self._heapify(nodes)
		self.max_height = self.max_depth()
		self.index_of_leaves = \
			self.get_leftmost(self.max_height)


	def __repr__(self):
		'''(ImplicitKDTree) -> str.'''

		return str(self.nodes[0])


	def _heapify(self, nodes):
		'''(ImplicitKDTree, list of tuples) -> NoneType
		'Heapify' the nodes of ImplicitKDTree in place.'''

		for i in range(1, self.num):
			self._bubble_up(nodes, i)


	def _bubble_up(self, L, i):
		'''(ImplicitKDTree, list of tuples, int) -> NoneType.'''

		#while there is a parent and L[i] > its parent:
		#direction of inequality determines if heap is min or max
		#'>' for max, '<' for min.
		while (i > 0) and (L[i][self.depth(i) % self.dim] < \
		L[self._parent(i)][self.depth(self._parent(i)) % self.dim]):
			L[i], L[self._parent(i)] = L[self._parent(i)], L[i]
			i = self._parent(i)


	def _parent(self, i):
		'''(ImplicitKDTree, int) -> int
		Return the index of the parent of index i in the tree.'''

		return (i - 1) / 2


	def _left_child(self, i):
		'''(ImplicitKDTree, int) -> int
		Return the index of the left child of index i in the tree.'''

		return 2 * i + 1


	def _right_child(self, i):
		'''(ImplicitKDTree, int) -> int
		Return the index of the right child of index i in the tree.'''

		return 2 * i + 2


	def depth(self, i, depth=0):
		'''(ImplicitKDTree, int, int) -> int
		Return the depth of the node at index i.'''

		if i:
			return self.depth(self._parent(i), depth + 1)
		return depth


	def max_depth(self):
		'''(ImplicitKDTree) -> int
		Return the max depth of ImplicitKDTree.'''

		return self.depth(self.num - 1)


	def at_depth(self, stop_depth, i=0, nodes=[], depth=0):
		'''(ImplicitKDTree, int, int, list of tuples, int) -> list of tuples
		Return a list of all nodes at depth stop_depth.'''

		#if node does not exist
		if i >= self.num:
			return nodes

		if depth == stop_depth:
			return nodes + [self.nodes[i]]
		return self.at_depth(stop_depth, self._left_child(i), nodes, depth +\
			1) + self.at_depth(stop_depth, self._right_child(i), nodes, depth + 1)


	def siblings(self, i):
		'''(ImplicitKDTree, int) -> list of tups
		Return the siblings of the node at index i.'''

		siblings = []
		if i < self.num:
			siblings = self.at_depth(self.depth(i))
			siblings.remove(self.nodes[i])
		return siblings


	def leaves(self):
		'''(ImplicitKDTree) -> list of tuples
		Return the leaves of the tree.'''

		return self.nodes[self.index_of_leaves:]


	def insert(self, node):
		'''(ImplicitKDTree, tuple) -> NoneType
		Insert tuple node into ImplicitKDTree.'''

		#if isinstance(node, tuple) and len(node) == self.dim:
		self.nodes.append(node)
		self._bubble_up(self.nodes, self.num)
		self.num += 1


	def remove(self):
		'''(ImplicitKDTree) -> NoneType
		Remove the root of ImplicitKDTree (which is either
		the max or min of the tree).'''

		#Remove root
		self.nodes[0] = self.nodes[-1]
		self.nodes = self.nodes[:-1]
		self.num -= 1
		#fix the rest
		self._bubble_down(0)


	def _bubble_down(self, i):
		'''(ImplicitKDTree, int) -> NoneType
		Bubble the item at index i in the tree down to where it belongs.'''

		# while there is at least one child and L[i] < either child:
		while self._left_child(i) < self.num and self._is_smaller(i):
			# swap with the smaller of its two children
			left = self._left_child(i)
			right = self._right_child(i)
			smaller = left
			#For min: self.axis(right) < self.axis(left) and larger -> smaller
			#For max: self.axis(right) > self.axis(left) and smaller -> smaller
			if right < self.num and \
			self.axis(right) < self.axis(left):
				smaller = right

			self.nodes[i], self.nodes[smaller] = self.nodes[smaller],\
				self.nodes[i]
			i = smaller


	def _is_smaller(self, i):
		'''(ImplicitKDTree, int) -> bool
		Return whether the node at i is smaller
		than the max of its children.'''

		left = self._left_child(i)
		max_index = left
		if left < self.num:
			axis_max = self.axis(max_index)
		right = self._right_child(i)
		axis_right = self.axis(right)
		#For min, axis_right < axis_max on next if block
		#For max, axis_max > axis_right on next if block
		if right < self.num and (axis_right < axis_max):
			#max_index = right
		#For max, the two following inequalities should be '<'
		#whereas for min, the inequalities would be '>'.
			return self.axis(i) > axis_right
		return self.axis(i) > axis_max


	def axis(self, i):
		'''(ImplicitKDTree, int) -> int
		Return the axis value of the node at index i.'''

		#First line not necessary if hard-coded to avoid index error
		#if i < self.num:
		return self.nodes[i][self.depth(i) % self.dim]


	def Node(self, i):
		'''(ImplicitKDTree, int) -> list
		Return a list of information of the node at index i.
		NOTE: only use this method for testing/visualization.'''

		if i < self.num:
			node = self.nodes[i]
			left_ind = self._left_child(i)
			if left_ind < self.num:
				left = self.nodes[left_ind]
			else:
				left = None
			right_ind = self._right_child(i)
			if right_ind < self.num:
				right = self.nodes[right_ind]
			else:
				right = None
				depth = self.depth(i)
				cut_val = node[depth % self.dim]
				return [node, left, right, cut_val]
		return []


	def merge(self, other):
		'''(ImplicitKDTree, ImplicitKDTree) -> NoneType
		Merge the two ImplicitKDTrees into ImplicitKDTree self.'''

		if isinstance(other, ImplicitKDTree):
			for node in other.nodes:
				self.nodes.append(node)
				self._bubble_up(self.nodes, self.num)
				self.num += 1


	def path(self, i):
		'''(ImplicitKDTree, int) -> list of tuples
		Return a list of successive nodes that compose the path from
		the node at index 0 (the root) to the node at index i.'''

		if i < self.num:
			return [self.nodes[0]] + self._path(i)
		return []


	def _path(self, i, nodes=[]):
		'''(ImplicitKDTree, int, list of tuples) -> list of tuples.'''

		if i:
			return self._path(self._parent(i), [self.nodes[i]] + nodes)
		return nodes


	def sqdist(self, i, node):
		'''(ImplicitKDTree, int, tuple) -> int
		Return the squared Euclidean distance between the node
		at index i and tuple node. Return -1 if i
		is not in ImplicitKDTree.'''

		if (i < self.num):
			if isinstance(node, tuple) and len(node) == self.dim:
				s = 0
				for k in range(self.dim):
					d = self.nodes[i][k] - node[k]
					s += d * d
				return s
		return -1


	def NNSearch(self, node, i=0, depth=0, best=float('inf'), nbest=None):
		'''(ImplicitKDTree, tuple, int, int, int, int) -> int.
		Return the index of the nearest neighbour of tuple node.'''

		if i >= self.num:
			return nbest

		axis = depth % self.dim
		dist = self.sqdist(i, node)
		if (dist < best):
			best = dist
			nbest = i
		diff = node[axis] - self.nodes[i][axis]
		(close, away) = (self._left_child(i), self._right_child(i)) if \
			diff <= 0 else (self._right_child(i), self._left_child(i))
		if close:
			return self.NNSearch(node, close, depth + 1, best, nbest)
		return nbest


	def lower_bound(self, i):
		'''(ImplicitKDTree, int) -> int
		Return the lower bound from index i.'''

		return self._lower_bound(i, self.depth(i) % self.dim)


	def _lower_bound(self, i, cut_dim, lowest=float('inf')):
		'''(ImplicitKDTree, int, int, int) -> int'''

		if i >= self.num:
			return lowest

		lowest = min(lowest, self.nodes[i][cut_dim])
		lowest = self._lower_bound(self._left_child(i), cut_dim, lowest)
		lowest = self._lower_bound(self._right_child(i), cut_dim, lowest)
		return lowest


	def upper_bound(self, i):
		'''(ImplicitKDTree, int) -> int
		Return the upper bound from index i.'''

		return self._upper_bound(i, self.depth(i) % self.dim)


	def _upper_bound(self, i, cut_dim, highest=0):
		'''(ImplicitKDTree, int, int, int) -> int'''

		if i >= self.num:
			return highest

		highest = max(highest, self.nodes[i][cut_dim])
		highest = self._upper_bound(self._left_child(i), cut_dim, highest)
		highest = self._upper_bound(self._right_child(i), cut_dim, highest)
		return highest


	def is_left(self, i):
		'''(ImplicitKDTree, int) -> bool
		Return whether the node at index i is a left child.'''

		return i == self._left_child(self._parent(i))


	def is_right(self, i):
		'''(ImplicitKDTree, int) -> bool
		Return whether the node at index i is a right child.'''

		return i == self._right_child(self._parent(i))


	def get_leftmost(self, depth):
		'''(ImplicitKDTree, int) -> int
		Return the index of the leftmost node at depth depth.'''

		index = 0
		result = 0
		while self.depth(index) < depth:
			index = self._left_child(index)
			if index < self.num:
				result = index
		return result


	def get_rightmost(self, depth):
		'''(ImplicitKDTree, int) -> int
		Return the index of the rightmost node at depth depth.'''

		index = 0
		result = 0
		while self.depth(index) < depth:
			index = self._right_child(index)
			if index < self.num:
				result = index
		return result


if __name__ == '__main__':
	nodes = []
	for i in range(0, 50000, 5):
	nodes.append((i, i + 1, i + 2, i + 3, i + 4))
	tree = ImplicitKDTree(nodes, 5)
	del nodes

	## TODO: make write_tree(), print_tree()
