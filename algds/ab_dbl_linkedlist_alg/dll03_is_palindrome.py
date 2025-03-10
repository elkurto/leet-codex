import unittest
import math

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

  def append_args(self, *args):
    for arg in args:
      self.append( arg )
    return self

  def is_palindrome(self):

    if self.head is None:
      return False

    a =self.head
    b =self.tail


    b_is_palindrome =True
    for i in range(0, math.floor( self.length/2) ):
      b_is_palindrome =(a.value == b.value)
      if not b_is_palindrome:
        break

      a =a.next
      b =b.prev
    #end-for-i

    return b_is_palindrome

class TestDoublyLinkedList(unittest.TestCase):
  def test_palindrome_empty_list(self):
    d =DoublyLinkedList(None)
    d.head =None
    d.tail =None
    d.length =0

    self.assertFalse( d.is_palindrome() )

  def test_palindrome_one_node(self):
    d =DoublyLinkedList(1)
    self.assertTrue( d.is_palindrome() )

  def test_palindrome_two_node_positive(self):
    d =DoublyLinkedList(3)
    d.append( 3 )
    # [3,3] is a palindrome
    self.assertTrue( d.is_palindrome() )

  def test_palindrome_two_node_negative(self):
    d =DoublyLinkedList(3)
    d.append(999)
    # [3,999] is not a palindrome
    self.assertFalse( d.is_palindrome() )

  def test_palindrome_five_node_positive(self):
    d =DoublyLinkedList(3).append_args(2,1,2,3)
    # [3,2,1,2,3] is a palindrome
    self.assertTrue( d.is_palindrome() )


  def test_palindrome_five_node_negative(self):
    d =DoublyLinkedList(3).append_args(2,1,999,3)
    # [3,2,1,999,3] is not a palindrome
    self.assertFalse( d.is_palindrome() )


if __name__ == "__main__":
  unittest.main()