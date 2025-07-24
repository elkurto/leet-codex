import unittest
from ..stack_fixed_type_size import StackFixedTypeAndSize

class TestStackFixedTypeAndSize(unittest.TestCase):
  def test_foo(self):
    self.assertTrue(True)

  def test_append(self):
    s =StackFixedTypeAndSize(int, 5)
    s.append( 3 )
    s.append( 4 )
    self.assertEquals( len(s), 2)

if __name__ == "__main__":
  unittest.main()