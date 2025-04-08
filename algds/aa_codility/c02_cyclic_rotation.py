import collections
import sys

"""
Move all elements in :list:ary to right by n elements.
To index=0, move ny elements that move past end of :list:ary
e.g.  cyclic_rotate_list_to_right([0,1,2,3,4], 1)
  // returns [ 4, 0,1,2,3]

e.g.  cyclic_rotate_list_to_right([0,1,2,3,4], 2)
  // returns [ 3,4, 0,1,2]

e.g.  cyclic_rotate_list_to_right([0,1,2,3,4], 3)
  // returns [ 2,3,4, 0,1]
  
"""

def cyclic_rotate_list_to_right(ary, n):
  d =collections.deque(ary)
  if len(d) > 0:
    m =n % len(ary)
    for _ in range(m):
      _rotate_right_by_one(d)

  return d


def _rotate_right_by_one(deq):
  x =deq.pop()
  deq.appendleft(x)


if __name__ == "__main__":
  ary =sys.argv[1:-1]
  n =int(sys.argv[-1])
  deq_rotated =cyclic_rotate_list_to_right(ary, n )
  print( 'deq_rotated = [{0}]'.format( deq_rotated))