import sys, os
path = os.path.join(os.path.join(os.path.join('..', '..'), 'Simple BST'), 'Regular')
sys.path.append(path)
from Node import *


def bf_update(root, inserted):
	current = inserted
	while(current.parent != current):
		if (current == current.parent.right):
			current.parent.bf += 1
			if (current.parent.bf == 2):
				root = AVL_Node.rotations[(2, current.bf)](current.parent)
		elif (current == current.parent.left):
			current.parent.bf -= 1
			if (current.parent.bf == -2):
				root = AVL_Node.rotations[(-2, current.bf)](current.parent)
		current = current.parent


def sleft_rot(root):
	moving = root.right.left 
	A, B = root, root.right
	
	root = B
	root.left = A
	A.right = moving
	
	#update parents of moved swapped subtrees
	if(A != A.parent):
		root.parent = A.parent
	else:
		root.parent = root
	A.parent = root

	if(moving):
		moving.parent = A
	
	#update balance factors
	A.bf = 0
	root.bf = 0
	return root


def drl_rot(root):
	pass


def dlr_rot(root):
	pass


def sright_rot(root):
	pass


class AVL_Node(Node):
	rotations = \
		{(2, 1): sleft_rot,
		(2, -1): drl_rot,
		(-2, 1): dlr_rot,
		(-2, -1): sright_rot}

	def __init__(self, key, left=None, right=None):
		super(AVL_Node, self).__init__(key, left, right)
		self.bf = 0


	#Overrides parent method
	def insert(self, val):
		self.__insert(val)


	def __insert(self, val):
		fnode = self.find(val)
		assert(fnode.key != val)

		if(val > fnode.key):
			fnode.right = AVL_Node(val)
			inserted = fnode.right
		else:
			fnode.left = AVL_Node(val)
			inserted = fnode.left
		
		inserted.parent = fnode
		bf_update(self, inserted)


	def print_bf(self):
		self._print_bf(self, '')


	def _print_bf(self, root, indent, i=1):
		if root:
			self._print_bf(root.right, indent + '        |' + str(i) + "| ", \
			i + 1)
			print indent + str(int(root.bf))
			self._print_bf(root.left, indent + '        |' + str(i) + "| ", \
			i + 1)


	#Overrides parent method
	def remove(self, val):
		assert(self.key != val)
		self.__remove(val)	


	def __remove(self, val):
		pass
