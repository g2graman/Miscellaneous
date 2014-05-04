class LList(object):
	def __init__(self, key=None):
		self.key = key
		self.tail = self	#for O(1) insertion
		self.next = None
		self.prev = self	#for O(1) predecessor
		#self.cargo		--> for augmentations


	def insert(self, val):
	'''(LList, object) -> None
	Insert object val into the end of the Linked List.'''
		
		self.tail.next.key = val
		self.tail.next.prev = self.tail
		self.tail = self.tail.next
		self.tail.tail = self.tail


	def remove(self, val):
	'''(LList, object) -> LList
	Remove val from the Linked List rooted at self and return the LList rooted at its
	predecessor.'''
		
		fnode = self.find(val)

		if(not(fnode)):
			#A node with key val was not found in the Linked Listed rooted at self
			return None

		if(fnode == self):
			#val is at the front of the List
			self = self.next
			self.prev = self
			return self

		if(fnode.next):
			#val was not found as the tail
			self.next.prev = self.prev
			self.prev.next = self.next
			return self.prev

		#If we have gotten here, val is the tail node
		self.tail = self.tail.prev
		self.tail.next = None
		return self.tail


	def find(self, val):
	'''(LList, object) -> LList
	Find and return the List rooted at val, otherwise return None.'''
		
		current = self #Alias to not lose the trail of the List
		tail = current.tail
		while(current.next && current.val != val):
			if (current.tail != tail):
				current.tail = tail
			current = current.next

		if(current.val == val):
			return current
		#return None	--> Happens by default
