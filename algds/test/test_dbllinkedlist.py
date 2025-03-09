import unittest
from algds.dbllinkedlist import DoubleLinkedList

class TestDoubleLinkedList(unittest.TestCase):

  
  def test_append(self):
    dllist =DoubleLinkedList()
    dllist.append(0)
    dllist.append(1)
    dllist.append(2)
    dllist.append(3)
    dllist.append(4)
    dllist.append(5)
    print(dllist)

    self.assertEqual(dllist.length, 6)
    self.assertEqual(dllist.head.value, 0)
    self.assertIsNone(dllist.head.prev)

    self.assertEqual(dllist.tail.value, 5)
    self.assertIsNone( dllist.tail.next)

  def test_pop_00_pop_many(self):
    dllist =DoubleLinkedList().append_args( 0,1,2,3,4,5,6 )
    self.assertEqual( dllist.length, 7)
    v =dllist.pop()
    self.assertEqual( v, 6 )
    self.assertEqual( dllist.length, 6)

    v =dllist.pop()
    self.assertEqual( v, 5 )
    v =dllist.pop()
    self.assertEqual( v, 4 )
    v =dllist.pop()
    self.assertEqual( v, 3 )
    v =dllist.pop()
    self.assertEqual( v, 2 )
    v =dllist.pop()
    self.assertEqual( v, 1 )
    v =dllist.pop()
    self.assertEqual( v, 0 )
    v =dllist.pop()
    self.assertIsNone( v )
    self.assertEqual( dllist.length, 0)
    self.assertIsNone( dllist.head )
    self.assertIsNone( dllist.tail )

    dllist.append(11)
    self.assertEqual( dllist.length, 1)
    self.assertEqual( dllist.head.value, 11)
    self.assertEqual( dllist.tail.value, 11)
    
    
  def test_prepend(self):
    dllist =DoubleLinkedList().append_args(1,2,3,4,5)

    dllist.prepend( 0 )
    self.assertEqual( dllist.head.value, 0 )
    self.assertEqual( dllist.head.next.value, 1 )
    self.assertEqual( dllist.length, 6)

  def test_prepend_to_empty_list(self):
    dllist =DoubleLinkedList()
    dllist.prepend( 999 )
    self.assertEqual( dllist.head.value, 999 )
    self.assertEqual( dllist.head.next, None )

  def test_pop_first(self):
    dllist =DoubleLinkedList().append_args(0,1,2,3)

    v =dllist.pop_first()
    self.assertEqual(v, 0)

    v =dllist.pop_first()
    self.assertEqual(v, 1)

    v =dllist.pop_first()
    self.assertEqual(v, 2)

    v =dllist.pop_first()
    self.assertEqual(v, 3)

    v =dllist.pop_first()
    self.assertIsNone(v)

  def test_insert(self):
    dllist =DoubleLinkedList().append_args(0,1,2,3,4,5)
    # insert middle
    dllist.insert(index=3, value=993)
    self.assertEqual( dllist.head.next.next.next.value, 993)
    self.assertEqual( dllist.length , 7)

    # insert first (index=0)
    dllist.insert(index=0, value=990)
    self.assertEqual( dllist.head.value, 990)
    self.assertEqual( dllist.length , 8)

    # insert last
    dllist.insert(index=dllist.length, value=997)
    self.assertEqual( dllist.tail.value, 997)
    self.assertEqual( dllist.length , 9)

    # insert second to last
    dllist.insert(index=dllist.length-1, value=444)
    self.assertEqual( dllist.tail.prev.value, 444)
    self.assertEqual( dllist.length , 10)

    # insert into empty list
    dllist =DoubleLinkedList()
    dllist.insert(index=0, value=555)
    self.assertEqual( dllist.head.value, 555)
    self.assertEqual( dllist.length , 1)


  def test_remove(self):
    # remove from empty list
    dllist =DoubleLinkedList()
    with self.assertRaises(IndexError):
      dllist.remove(0)

    # remove from list of length==1
    dllist =DoubleLinkedList().append_args( 0 )
    v =dllist.remove(0)
    self.assertEqual( v , 0)
    self.assertEqual( dllist.length , 0)

    # remove first when length==2
    dllist =DoubleLinkedList().append_args( 0, 1)
    v =dllist.remove(0)
    self.assertEqual( v , 0)
    self.assertEqual( dllist.length , 1)

    # remove last when length==2
    dllist =DoubleLinkedList().append_args( 0, 1 )
    v =dllist.remove(1)
    self.assertEqual( v , 1)
    self.assertEqual( dllist.length , 1)

    # remove first when length==3
    dllist =DoubleLinkedList().append_args( 0, 1, 2 )
    v =dllist.remove(0)
    self.assertEqual( v , 0)
    self.assertEqual( dllist.length , 2)

    # remove last when length==3
    dllist =DoubleLinkedList().append_args( 0, 1, 2 )
    v =dllist.remove(2)
    self.assertEqual( v , 2)
    self.assertEqual( dllist.length , 2)

    # remove middle when length==3
    dllist =DoubleLinkedList().append_args( 0, 1, 2)
    v =dllist.remove(1)
    self.assertEqual( v , 1)
    self.assertEqual( dllist.length , 2)


if __name__ == "__main__":
  unittest.main()