class Node(object):
	dim = 5

	def __init__(self, x, y, r=0, g=0, b=0, left=None, right=None):
		'''(Node, int, int, int, int, int, Node, Node) -> NoneType
		Make a new Node.'''

		self.p = [x, y, r, g, b]
		self.left = left
		self.right = right
		self.cargo = None
		self.lower = None
		self.upper = None


	def sqdist(self, other):
		'''(Node, Node) -> int
		Return the squared Euclidean distance of Node self and Node other.'''

		if self and other:
		s = 0
		for i in range(len(self.p)):
		d = self.p[i] - other.p[i]
		s += d * d
		return s
		return -1


	def __repr__(self):
		'''(Node) -> str
		Return the str representation of Node.'''

		return self._repr()


	def _repr(self, rep='{', i=0):
		'''(Node, str, int) -> str.'''

		if self.p[:-(i + 1)]:
		return self._repr(rep + str(self.p[i]) + ", ", i + 1)
		return rep + str(self.p[i]) + "}"


	def flat(self):
		'''(Node) -> Node
		Return the root Node of a heap that represents all nodes
		descending from Node self which directly compare argo.'''

		return [self] + self._flat(self, [])


	def _flat(self, root, tree=[]):
		'''(Node, Node, list of Nodes) -> list of Nodes
		Return a list of nodes rooted at Node root.'''

		if root:
			if root.left:
				tree.append(root.left)
				self._flat(root.left, tree)
			if root.right:
				tree.append(root.right)
				self._flat(root.right, tree)
			return tree
		return tree


	def children(self):
		'''(Node) -> list of Nodes
		Return the children of Node self.'''

		#Takes advantage of KDTree structure by checking
		#Node.left first.

		children = []
		if self.left:
			children.append(self.left)
		if self.right:
			children.append(self.right)
		return children


	def has_children(self):
	'''(Node) -> bool
	Return whether Node self has children.'''

	return bool(self.children())
