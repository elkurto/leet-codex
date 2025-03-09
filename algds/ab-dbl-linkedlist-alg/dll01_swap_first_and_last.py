import unittest

"""
Problem Statement from Leet_Code
Swap the values of the first and last node

Method name:
swap_first_last

Note that the pointers to the nodes themselves are not swapped 
  - only their values are exchanged.
"""
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None


class DoublyLinkedList:
  def __init__(self, value):
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
    self.length = 1

  def print_list(self):
    temp = self.head
    while temp is not None:
      print(temp.value)
      temp = temp.next

  def append(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
    self.length += 1
    return True

  def swap_first_last(self):
    if self.head is None:
      #case empty
      return
    elif self.head == self.tail:
      #case length == 1
      return
    else:
      #case length >= 2
      temp =self.head.value
      self.head.value =self.tail.value
      self.tail.value =temp

class TestDoublLinkedList(unittest.TestCase):
  def test_empty_list(self):
    d =DoublyLinkedList(None)
    d.head =None
    d.tail =None
    d.length =0

    d.swap_first_last()
    self.assertIsNone( self.head )
    self.assertIsNone( self.tail )

  def test_case_length_eq_01(self):
    d =DoublyLinkedList(0)
    d.swap_first_last()
    self.assertEqual( d.head.value, 0)
    self.assertEqual( d.tail.value, 0)


  def test_case_length_eq_02(self):
    d =DoublyLinkedList(0)
    d.append(1)
    # d =[0,1]

    d.swap_first_last()
    # d =[1,0]
    self.assertEqual( d.head.value, 1)
    self.assertEqual( d.tail.value, 0)


  def test_case_length_eq_06(self):
    d =DoublyLinkedList(0)
    d.append( 1 )
    d.append( 2 )
    d.append( 3 )
    d.append( 4 )
    d.append( 5 )
    # d =[0,1,2,3,4,5]

    d.swap_first_last()
    # d =[5,1,2,3,4,0]
    self.assertEqual( d.head.value, 5)
    self.assertEqual( d.tail.value, 0)


if __name__ == "__main__":
  unittest.main()