class Stack(object): 
	def __init__(self) : 
		self.elements = []
		self.length = 0


	def push(self, element): 
		self.elements.append(element)
		self.length += 1 


	def pop(self):
		if (not(self.is_empty())):
			self.length -= 1
			return self.elements.pop()


	def peek(self):
		if (not(self.is_empty())):
			return self.elements[0]


	def is_empty(self): 
		return self.length == 0


	def __repr__(self):
		return str(self.elements)
