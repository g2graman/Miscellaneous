from Stack import *


class Queue_from_Stacks(object): 
  def __init__(self): 
    self.in_stack = Stack()
    self.out_stack = Stack()
    self.length = 0


  def is_empty(self): 
    return self.length <= 0 


  def enqueue(self, element):
    self.in_stack.push(element)
    self.length += 1 


  def dequeue(self):
    if(self.out_stack.is_empty()):
      while (not(self.in_stack.is_empty())):
        self.out_stack.push(self.in_stack.pop())
    if (not(self.out_stack.is_empty())):
      self.length -= 1
      return self.out_stack.pop()


  def __repr__(self):
    return "IN: " + str(self.in_stack) + "\nOUT: " + str(self.out_stack)
