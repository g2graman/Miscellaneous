class Stack(list):
    '''A last-in, first-out (LIFO) stack of items'''


    def __init__(self):
        '''(Stack) -> NoneType
        A new empty Stack.
        '''

        self.contents = []


    def push(self, v):
        '''(Stack, object) -> NoneType
        Make v the new top object on this stack.
        '''

        self.contents.append(v)


    def pop(self):
        '''(Stack) -> object
        Remove and return the top item on this Stack.
        '''

        return self.contents.pop()


    def is_empty(self):
        '''(Stack) -> bool
        Return whether this Stack is empty.
        '''

        return not self.contents
