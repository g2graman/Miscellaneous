import sys, os
path = os.path.join(os.path.join(os.path.join('..', '..'), 'Simple BST'), 'Regular')
sys.path.append(path)
from Node import *


class AVL_Node(Node):
	def __init__(self, key, left=None, right=None):
		super(AVL_Node, self).__init__(key, left, right)
		self.balance_factor = 0
		self.height = 0


	def insert(self, val):
		self.__insert(val)


	def __insert(self, val):
		pass


	def remove(self, val):
		assert(self.key != val)
		self.__remove(val)	


	def __remove(self, val):
		pass

	
	#TODO: Rotations!
