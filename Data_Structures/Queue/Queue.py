class Queue(object): 
  def __init__(self): 
    self.length = 0 
    self.items = []
    self.head = 0


  def is_empty(self): 
    return (self.get_size() <= 0) 


  def enqueue(self, element):
    self.items.append(element)
    self.length += 1 


  def dequeue(self):
    old_head = self.head
    if (self.length > 0):
      self.head += 1
    else:
      if (self.head <= self.length):
        if (self.length == 0):
          self.items = []
          self.head = 0
    return self.items[old_head]


  def __repr__(self):
    if(0 <= self.head < self.length):
      return str(self.items[self.head:])
    return str([])


  def get_size(self):
    return self.length - self.head
