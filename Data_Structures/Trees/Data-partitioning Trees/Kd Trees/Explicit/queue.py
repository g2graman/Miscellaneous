class Queue(object):
	'''A first-in first-out (FIFO) data structure.'''


	def __init__(self):
		'''(Queue) -> NoneType
		Make a new empty queue.'''

		self._queue = []


	def enqueue(self, o):
		'''(Queue, object) -> NoneType
		Put o at the end of this queue.'''

		self._queue.append(o)


	def front(self):
		'''(Queue) -> object
		Return the item that has been in this queue the longest.'''

		return self._queue[0]


	def dequeue(self):
		'''(Queue) -> object
		Remove and return the front item.'''

		return self._queue.pop(0)


	def is_empty(self):
		'''(Queue) -> bool
		Return whether there are any items in this queue.'''

		return self._queue == []
