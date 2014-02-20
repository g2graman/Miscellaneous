from Queue import *


class Stack_from_Queues(object):
	def __init__(self):
		self.in_queue = Queue()
		self.out_queue = Queue()
		self.length = 0


	def push(self, element):
		self.in_queue.enqueue(element)
		self.length += 1


	def pop(self):
		while(self.in_queue.get_size() > 1):
			element = self.in_queue.dequeue()
			if (element):	#Check if not None
				self.out_queue.enqueue(element)

		if (self.in_queue.get_size() == 1):
			self.length -= 1
			return self.in_queue.dequeue()
		elif (self.out_queue.get_size() > 0):
			self.length -= 1
			return self.out_queue.dequeue()


	def is_empty(self):
		return self.length <= 0


	def __repr__(self):
		return "IN: " + str(self.in_queue) + "\nOUT: " + str(self.out_queue)
