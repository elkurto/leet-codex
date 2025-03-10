import unittest
from algds.stack_linkedlist import StackLinkedList


class TestStackLinkedList(unittest.TestCase):
  def test_push(self):
    s =StackLinkedList()
    s.push(0)
    s.push(1)
    s.push(2)

    self.assertEqual(s.height, 3)
    self.assertEqual(s.top.value, 2)

  def test_pop(self):
    s =StackLinkedList()
    s.push(0)
    s.push(1)
    s.push(2)

    self.assertEqual(s.height, 3)

    v =s.pop()
    self.assertEqual( v, 2 )
    v =s.pop()
    self.assertEqual( v, 1)
    v=s.pop()
    self.assertEqual( v, 0)
    v=s.pop()
    self.assertIsNone( v )

if __name__ == '__main__':
  unittest.main()