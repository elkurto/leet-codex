import unittest
from algds.queue_linkedlist import QueueLinkedList


class TestQueueLinkedList(unittest.TestCase):
  def test_push(self):
    q =QueueLinkedList()
    q.push(0)
    q.push(1)
    q.push(2)

    self.assertEqual(q.length, 3)
    self.assertEqual(q.head.value, 2)

  def test_pop(self):
    q =QueueLinkedList()
    q.push(0)
    q.push(1)
    q.push(2)

    self.assertEqual(q.length, 3)

    v =q.pop()
    self.assertEqual( v, 0 )
    v =q.pop()
    self.assertEqual( v, 1)
    v=q.pop()
    self.assertEqual( v, 2)
    v=q.pop()
    self.assertIsNone( v )

if __name__ == '__main__':
  unittest.main()