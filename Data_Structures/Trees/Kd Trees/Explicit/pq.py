class PriorityQueue(object):
    '''A binary heap-based Priority Queue.'''


    def __init__(self):
        '''(PriorityQueue) -> NoneType.'''

        self._queue = []
        self._size = 0


    def enqueue(self, obj, priority):
        '''(PriorityQueue, object, int) -> NoneType.
        Enqueue object into PriorityQueue.'''

        self._queue.append((obj, priority))
        self._bubble_up(self._size)
        self._size += 1


    def dequeue(self):
        '''(PriorityQueue) -> object
        Dequeue PriorityQueue.'''

        front = self.front()
        self._queue[0] = self._queue[-1]
        self._queue = self._queue[:-1]
        self._size -= 1
        if not self.is_empty():
            self._bubble_down(0)
        return front


    def front(self):
        '''(PriorityQueue) -> object
        Return the front of PriorityQueue.'''

        return self._queue[0]


    def size(self):
        '''(PriorityQueue) -> int
        Return the size of PriorityQueue.'''

        return self._size


    def is_empty(self):
        '''(PriorityQueue) -> bool
        Return whether or not PriorityQueue is empty.'''

        return not(self._size)


    def _parent(self, i):
        '''(PriorityQueue, int) -> int
        Return the parent index of the index i.'''

        return (i - 1) / 2


    def _bubble_up(self, i):
        '''(PriorityQueue, int) -> NoneType.'''

        while (i > 0) and (self._queue[i][1] < \
            self._queue[self._parent(i)][1]):

            smaller = self._queue[i]
            larger = self._queue[self._parent(i)]
            #Swap
            smaller, larger = larger, smaller
            i = self._parent(i)


    def _left_child(self, i):
        '''(PriorityQueue, int) -> int
        Return the index of the left child of index i in the queue.'''

        return 2 * i + 1


    def _right_child(self, i):
        '''(PriorityQueue, int) -> int
        Return the index of the right child of index i in the queue.'''

        return 2 * i + 2


    def _bubble_down(self, i):
        '''(PriorityQueue, int) -> NoneType
        Bubble the item at index i in the queue down to where it belongs.'''

        while self._left_child(i) < self.size and self._is_smaller(i):
            left = self._left_child(i)
            right = self._right_child(i)
            smaller = left
            if right < self._size and \
            self.priority(right) < self.priority(left):
                smaller = right

            small = self._queue[smaller]
            large = self._queue[i]
            #Swap
            large, small = small, large
            i = smaller


    def priority(self, i):
        '''(PriorityQueue, int) -> int
        Return the priority of the object at index i.'''

        return self._queue[i][1]


    def _is_smaller(self, i):
        '''(PriorityQueue, int) -> bool
        Return whether the node at i is smaller
        than the max of its children.'''

        left = self._left_child(i)
        max_index = left
        if left < self._size:
            priority_max = self.priority(max_index)
        right = self._right_child(i)
        if right < self._size:
            priority_right = self.priority(right)
            if(priority_right < priority_max):
                max_index = right
                return self.priority(i) > priority_right
        return self.priority(i) > priority_max
