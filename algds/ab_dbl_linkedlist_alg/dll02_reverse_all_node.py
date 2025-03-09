import unittest
"""
Problem statement from Leet Code:

DLL: Reverse ( ** Interview Question)
Create a new method called reverse that reverses the order
of the nodes in the list, i.e., the first node becomes the last node,
the second node becomes the second-to-last node, and so on.

To do this, you'll need to traverse the list and change
the direction of the pointers between the nodes
so that they point in the opposite direction.

Do not change the value of any of the nodes.

Once you've done this for all nodes,
you'll also need to update the head and tail pointers
to reflect the new order of the nodes.


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

  @classmethod
  def swap_node(cls, a, b):
    if a == b:
      pass
    elif a is None:
      pass
    elif b is None:
      pass
    else:
      b_prev_orig =b.prev
      b_next_orig =b.next

      a_prev_orig =a.prev
      a_next_orig =a.next

      b_prev_orig.next =a
      a.prev =b_prev_orig

      a_next_orig.prev =b
      b.prev =a_prev_orig

      if b_next_orig:
        b_next_orig.prev =a

      if a_prev_orig:
        a_prev_orig.next =b


  def reverse(self):

    s =0
    e =self.length -1

    a =self.head
    b =self.tail
    while s < e:

      self.swap_node( a, b )
      a =b.next
      b =a.prev

      s+=1
      e-=1

class TestDoublLinkedList(unittest.TestCase):
  def test_empty_list(self):
    pass

  def test_case_length_eq_1(self):
    pass
  def test_case_length_eq_2(self):
    pass
  def test_case_length_eq_5(self):
    pass

if __name__ == "__main__":
  unittest.main()