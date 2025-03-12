import unittest

"""
Given an array a, your task is to output an array b of
  the same length by applying the following transformation:
– For each i from 0 to a.length - 1 inclusive,
   b[i] = a[i - 1] + a[i] + a[i + 1]
– If an element in the sum a[i - 1] + a[i] + a[i + 1] does not exist,
   then use 0 in its place
– For instance, b[0] = 0 + a[0] + a[1]

Example

For a = [4, 0, 1, -2, 3]:
– b[0] = 0 + a[0] + a[1] = 0 + 4 + 0 = 4
– b[1] = a[0] + a[1] + a[2] = 4 + 0 + 1 = 5
– b[2] = a[1] + a[2] + a[3] = 0 + 1 + (-2) = -1
– b[3] = a[2] + a[3] + a[4] = 1 + (-2) + 3 = 2
– b[4] = a[3] + a[4] + 0 = (-2) + 3 + 0 = 1

So, the output should be solution(a) = [4, 5, -1, 2, 1].

(@see Question 1: https://codesignal.com/blog/interview-prep/example-codesignal-questions/)
"""

class AryManipulator:
  @classmethod
  def compute_solution(cls, ai):
    """
    :param ai: a list of ints
    :return:  b:ary - a list of sums
       b[i] =ai[i-1] + ai[i] + ai[i+1]
       if ai[i-1] is out of bounds then substitute 0
       if ai[i+1] is out of bounds then substitute 0
    """
    b =[]
    for i in range(0,len(ai)):
      ai_minus_01 =cls.fetch_at_index_or_default( ary=ai, index=i-1, default_value=0)
      ai_i = ai[i]
      ai_plus_01 =cls.fetch_at_index_or_default( ary=ai, index=i+1, default_value=0)
      b.append( ai_plus_01 + ai_i + ai_minus_01)

    return b

  @classmethod
  def fetch_at_index_or_default(cls, ary, index, default_value=0):
    value =default_value
    if 0 <= index < len(ary):
      value =ary[index]
    return value


class TestAryManipulator(unittest.TestCase):
  def test_simple(self):
    b =AryManipulator.compute_solution( [4,0,1,-2,3] )
    self.assertListEqual( b, [4,5,-1,2,1])

  def test_middle(self):
    b =AryManipulator.compute_solution( [4,0,1,-2,3,99,100] )
    self.assertListEqual( b, [4,5,-1,2,100,202,199])

  def test_empty(self):
    b =AryManipulator.compute_solution( [] )
    self.assertListEqual( b, [])

if __name__ == "__main__":
  unittest.main()