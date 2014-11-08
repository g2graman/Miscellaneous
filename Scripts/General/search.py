def sort(L):
  '''(list) -> list

  Returns a sorted version of list L, where every element in L
  must have the same number of dimensions.'''

  m_len = len(max(L, key=len))
  assert(all([len(x) == m_len for x in L])) #Make sure all elements have same length
  return _sort(L, 0, m_len)


def _sort(L, dim, m_dim=0):
  '''(list, int, int) -> list

  Recursively merge sort list L, where every element has int m_dim
  dimensions, starting from int dimension dim.'''

  if(len(L) <= 1):
    return L

  left, right = [], []
  mid = len(L) / 2
  
  '''TODO: Replace with selection algorithm for finding median in O(n) instead of having to sort data along every cutting axis.
  For O(n + klog(n)) complexity of finding k order statistics, bulk load a min-max heap. 
  
  http://cglab.ca/~morin/teaching/5408/refs/minmax.pdf
  '''
  med = sorted(L, key=lambda x: x[dim])[mid][dim] #Find the median along the cutting axis

  left = [x for x in L if x[dim] < med]
  right = [x for x in L if x[dim] > med]
  result = list(set(L) - set(left + right))

  left = _sort(left, (dim + 1) % m_dim, m_dim)
  right = _sort(right, (dim + 1) % m_dim, m_dim)
  result = left + result + right
  return result


def search(L, elem):
  '''(list, object) -> object

  Precondition: list L is sorted as per the above definition
  of being sorted.

  Perform higher dimensional binary search for element elem in list L,
  returning the closest element found.'''

  m_len = len(max(L, key=len))
  assert(all([len(x) == m_len for x in L]) and len(elem) == m_len)

  temp = L[:]
  dim = 0;
  while(len(temp) > 1):
    mid = len(temp) / 2
    if (elem[dim] <= temp[mid][dim]):
      temp = temp[:mid+1]
    else:
      temp = temp[mid+1:]

  if temp == []:
    return None
  return temp[0]
