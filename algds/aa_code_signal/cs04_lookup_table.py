import unittest
import re
"""

Given an array of unique integers numbers, your task is to find
the number of pairs of indices (i, j)  such that
a, i ≤ j and
b. the sum numbers[i] + numbers[j] is equal to some power of 2.


Note: The numbers 20  = 1, 21 = 2, 22 = 4, 23 = 8, etc.
are considered to be powers of 2.

Example

For numbers = [1, -1, 2, 3], the output should be solution(numbers) = 5.
– There is one pair of indices where the sum of the elements is 20 = 1:

"""

class LookUpTableReporter:

  @classmethod
  def print_report_line(cls, i, j, ni, nj):
    msg =("({i},{j}): numbers[{i}] + number[{j}] = {ni} + {nj} = {sum}"
          ).format( i=i, j=j, ni=ni, nj=nj, sum=ni+nj)
    print(msg)

  @classmethod
  def is_power_of_2(cls, num):

    sbin =bin(num)
    b_is_power_of_2 =(0 == num) or (re.match("^0b10*$", sbin) is not None)
    return b_is_power_of_2

  @classmethod
  def scan_and_report(cls, numbers):
    list_index_pair =[]
    for i in range(0,len(numbers)):
      for j in range(i, len(numbers)):
        ni =numbers[i]
        nj =numbers[j]
        if cls.is_power_of_2(ni + nj):
          cls.print_report_line(i,j,ni,nj)

          list_index_pair.append( (i,j,ni,nj) )
        #end-if

    return list_index_pair

class TestLookUpTableReporter(unittest.TestCase):
  def test_case_1(self):
    pairs =LookUpTableReporter.scan_and_report([2,1,0])
    self.assertEqual( len(pairs), 5)
    #                                        i,j,ni, nj
    self.assertTupleEqual( pairs[0], (0,0, 2, 2))
    self.assertTupleEqual( pairs[1], (0,2, 2, 0))
    self.assertTupleEqual( pairs[2], (1,1, 1, 1))
    self.assertTupleEqual( pairs[3], (1,2, 1, 0))
    self.assertTupleEqual( pairs[4], (2,2, 0, 0))

  def test_case_2(self):
    pairs =LookUpTableReporter.scan_and_report([2,15,0,22])
    self.assertEqual( len(pairs), 3)
    #                                        i,j,ni, nj
    self.assertTupleEqual( pairs[0], (0,0, 2, 2))
    self.assertTupleEqual( pairs[1], (0,2, 2, 0))
    self.assertTupleEqual( pairs[2], (2,2, 0, 0))


if __name__ == "__main__":
  unittest.main()