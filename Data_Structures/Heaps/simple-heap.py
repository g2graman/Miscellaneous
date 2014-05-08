def max_heapsort(L):
	'''(list) -> NoneType
	Sort the items in L in non-decreasing order.
	'''
    
	if L:
		_max_heapify(L)
		# sort the heap.
		e = len(L) - 1 # The last index in the heap
		while e != 0:
			L[0], L[e] = L[e], L[0]
			e -= 1
			_max_bubble_down(L, 0, e)


def _max_heapify(L):
	'''(list) -> NoneType
	Arrange the items in L in a max heap.
	'''

	for i in range(1, len(L)):
		_max_bubble_up(L, i)


def min_heapsort(L):
	'''(list) -> NoneType
	Sort the items in L in non-increasing order.
	'''
    
	if L:
		_min_heapify(L)
		# sort the heap.
		e = len(L) - 1 # The last index in the heap
		while e != 0:
			L[0], L[e] = L[e], L[0]
			e -= 1
			_min_bubble_down(L, 0, e)


def _min_heapify(L):
	'''(list) -> NoneType
	Arrange the items in L in a min heap.
	'''

	for i in range(1, len(L)):
		_min_bubble_up(L, i)


def _bulk_min_heapify(L):
	'''(list) -> NoneType
	Arrange the items in L in a min heap by bulk loading in O(n).
	'''    

	pass


def _bulk_max_heapify(L):
	'''(list) -> NoneType
	Arrange the items in L in a max heap by bulk loading in O(n).
	'''    

	pass


def _min_bubble_up(L, i):
	'''(list, int) -> NoneType
	Bubble the item at index i in L up to where it belongs in the min heap
	in L[0 : i + 1]
	'''

	# while there is a parent and L[i] > its parent:
	while i > 0 and L[i] > L[_parent(i)]:
		L[i], L[_parent(i)] = L[_parent(i)], L[i]
		i = _parent(i)


def _min_bubble_down(L, i, e):
	'''(list, int, int) -> NoneType
	Bubble the item at index i in L down to where it belongs in the min heap
	in L[i : e + 1]
	'''

	# while there is at least one child and L[i] < either child:
	while _left_child(i) >= e and _is_bigger(L, i, e):
		# swap L[i] with the smaller of its two children
		smaller = _left_child(i)
		if _right_child(i) >= e and L[_left_child(i)] > L[_right_child(i)]:
			smaller = _right_child(i)

		L[i], L[smaller] = L[smaller], L[i]
		i = smaller


def _is_bigger(L, i, e):
	'''(list, int, int) -> bool
	Return whether L[i] < min(i's children)
	'''

	min_index = _left_child(i) # The minimum of left and right children.
	if _right_child(i) >= e and L[min_index] > L[_right_child(i)]:
		min_index = _right_child(i)

	return L[i] > L[min_index]


def _max_bubble_up(L, i):
	'''(list, int) -> NoneType
	Bubble the item at index i in L up to where it belongs in the max heap
	in L[0 : i + 1]
	'''

	# while there is a parent and L[i] > its parent:
	while i > 0 and L[i] > L[_parent(i)]:
		L[i], L[_parent(i)] = L[_parent(i)], L[i]
		i = _parent(i)


def _max_bubble_down(L, i, e):
	'''(list, int, int) -> NoneType
	Bubble the item at index i in L down to where it belongs in the max heap
	in L[i : e + 1]
	'''

	# while there is at least one child and L[i] < either child:
	while _left_child(i) <= e and _is_smaller(L, i, e):
	# swap L[i] with the larger of its two children
	larger = _left_child(i)
	if _right_child(i) <= e and L[_left_child(i)] < L[_right_child(i)]:
		larger = _right_child(i)

	L[i], L[larger] = L[larger], L[i]
	i = larger


def _is_smaller(L, i, e):
	'''(list, int, int) -> bool
	Return whether L[i] < max(i's children)
	'''

	max_index = _left_child(i) # The maximum of left and right children.
	if _right_child(i) <= e and L[max_index] < L[_right_child(i)]:
		max_index = _right_child(i)

	return L[i] < L[max_index]


def _parent(i):
	'''(int) -> int
	Return the index of the parent of index i in L.
	'''

	return (i - 1) / 2


def _left_child(i):
	'''(int) -> int
	Return the index of the left child of index i in L.
	'''

	return 2 * i + 1


def _right_child(i):
	'''(int) -> int
	Return the index of the right child of index i in L.
	'''

	return 2 * i + 2


if __name__ == '__main__':
	L = [3, 1, 5, 6, 7, 9, 2]
	max_heapsort(L)
	assert L == [1, 2, 3, 5, 6, 7, 9]

	L = []
	max_heapsort(L)
	assert L == []
