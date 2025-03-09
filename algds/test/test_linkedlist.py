import unittest
import algds.linkedlist

class TestLinkedList(unittest.TestCase):
  def test_normal_push__pop_count(self):
    llist =algds.linkedlist.LinkedList()
    llist.push(5)
    llist.push(6)
    llist.push(7)

    self.assertEqual( llist.size(), 3 )
    self.assertEqual(5,llist.head.value)
    self.assertEqual(6,llist.head.next.value)
    self.assertEqual(7,llist.tail.value)

    value =llist.pop()
    self.assertEqual( 7 , value )

    value =llist.pop()
    self.assertEqual( 6, value )

    self.assertEqual( 1 , llist.size() )
    self.assertIs( llist.head, llist.tail)

    value =llist.pop()
    self.assertEqual( llist.size(), 0 )
    self.assertEqual( value, 5)

    value =llist.pop()
    self.assertIsNone( value )
    self.assertEqual( llist.size(), 0 )

  def test_push_pop_empty(self):
    llist =algds.linkedlist.LinkedList()
    llist.push(5)
    self.assertEqual( llist.head.value, 5)
    self.assertEqual( llist.tail.value, 5)

    value =llist.pop()
    self.assertEqual( value, 5)
    self.assertIsNone( llist.head)
    self.assertIsNone( llist.tail)

    value =llist.pop()
    self.assertIsNone( value )


  def test_push_first(self):
    llist =algds.linkedlist.LinkedList()
    llist.push_first(5)
    llist.push_first(6)
    llist.push_first(7)

    self.assertEqual( llist.head.value, 7)
    self.assertEqual( llist.head.next.value, 6)
    self.assertEqual( llist.head.next.next.value, 5)

    self.assertEqual( llist.tail.value , 5)


  def test_pop_first(self):
    llist =algds.linkedlist.LinkedList()
    llist.push_first(5)
    llist.push_first(6)
    llist.push_first(7)

    value =llist.pop_first()
    self.assertEqual( value, 7)

    value =llist.pop_first()
    self.assertEqual( value, 6)

    value =llist.pop_first()
    self.assertEqual( value, 5)


  def test__get_node_at_index(self):
    llist =algds.linkedlist.LinkedList()
    llist.push(5)
    llist.push(6)
    llist.push(7)
    llist.push(8)
    llist.push(9)

    node =llist._get_node_at_index(0)
    self.assertEqual( node.value, 5 )

    node =llist._get_node_at_index(2)
    self.assertEqual( node.value, 7 )

    node =llist._get_node_at_index(4)
    self.assertEqual( node.value, 9 )


  def test_set_value_at_index(self):
    llist =algds.linkedlist.LinkedList()
    llist.push(5)
    llist.push(6)
    llist.push(7)
    llist.push(8)
    llist.push(9)


    self.assertEqual( llist.at(0), 5 )

    llist.set_value_at_index(17, 2)
    self.assertEqual( llist.at(2), 17)

    llist.set_value_at_index(19, 4)
    self.assertEqual( llist.at(4), 19)

    llist.set_value_at_index(15, 0)
    self.assertEqual( llist.at(0), 15)

  def test_insert_value_at_index(self):
    llist =algds.linkedlist.LinkedList()
    llist.push_all(5,6,7,8,9)

    self.assertEqual( llist.size(), 5)

    llist.insert_value_at_index( 99, 0)
    self.assertEqual( llist.head.value, 99)
    self.assertEqual( llist.at(0), 99)
    self.assertEqual( llist.size(), 6)

    llist.insert_value_at_index( 97, 3)
    self.assertEqual( llist.size(), 7)
    self.assertEqual( llist.at(3), 97)
    node02 =llist._get_node_at_index(2)
    self.assertEqual( node02.value, 6)
    self.assertEqual( node02.next.value, 97)
    self.assertEqual( node02.next.next.value, 7)

    llist.insert_value_at_index( 100, llist.size()-1)
    self.assertEqual( llist.size(), 8)
    self.assertEqual( llist.tail.value, 9)
    self.assertEqual( llist.at(llist.size()-2), 100)

    llist.insert_value_at_index( 101, llist.size())
    self.assertEqual( llist.size(), 9)
    self.assertEqual( llist.tail.value, 101)




if __name__ == '__main__':
  unittest.main()
