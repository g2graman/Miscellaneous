from random import randint


class SkipList(object):
	def __init__(self, height=0, key=None):
		self.key = key
		self.next = [None]*height
		#self.cargo		-- For augmentations


	def randheight(self):
		'''(SkipList) -> int
		Return a random height.

		Precondition: the probability of an element having a height differing by 1
		is p=0.5'''

		h = 0
		while(randint(0,1) > 0):
			h += 1
		return h


	def _find_list(self, key):
		l = len(self.next)
		flist = [None]*l
		current = self
		for i in range(l-1, 0, -1):
			while(current.next[i] and current.next[i].key < key):
				current = current.next[i]
        	flist[i] = current
		return flist


	def find(self, key):
		flist = self._find_list(key)
		if(len(flist) > 0 and flist[0]):
			candidate = flist[0].next[0]
			if (candidate and candidate.key == key):
				return candidate


	def insert(self, key):
		node = SkipList(self.randheight(), key)
		while(len(self.next) < len(node.next)):
			self.next.append(None)
 
		flist = self._find_list(key)            
		if not(self.find(key)):
			for i in range(len(node.next)):
				if(flist[i]):
					node.next[i] = flist[i].next[i]
					flist[i].next[i] = node


	def remove(self, key):
		flist = self.find(key)
		if (flist):
			for i in range(len(flist.next)):
				flist[i].next[i] = flist.next[i]


	def __repr__(self):	#TODO: FIX THIS
		return str(self.key) + "\n" + self.next.__repr__()
