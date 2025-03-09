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

    elif a.next == b and b.prev == a:
      #   a <--> b
      a_prev_orig =a.prev
      b_next_orig =b.next

      if a_prev_orig:
        a_prev_orig.next =b
      if b_next_orig:
        b_next_orig.prev =a

      b.next =a
      a.prev =b

      a.next =b_next_orig
      b.prev =a_prev_orig


    elif b.next == a and a.prev == b:
      #   b <--> a
      cls.swap_node( b, a )

    else:
      # save original references
      b_prev_orig =b.prev
      b_next_orig =b.next

      a_prev_orig =a.prev
      a_next_orig =a.next

      # link a
      if b_prev_orig:
        b_prev_orig.next =a
      a.prev =b_prev_orig

      if b_next_orig:
        b_next_orig.prev =a
      a.next =b_next_orig

      # link b
      if a_prev_orig:
        a_prev_orig.next =b
      b.prev =a_prev_orig

      if a_next_orig:
        a_next_orig.prev =b
      b.next =a_next_orig


  def reverse(self):

    s =0
    e =self.length -1

    a =self.head
    b =self.tail
    while s < e:

      self.swap_node( a, b )
      if s == 0:
        self.head =b
        self.tail =a

      s+=1
      e-=1

      temp_a =a
      a =b.next
      b =temp_a.prev

class TestDoublLinkedList(unittest.TestCase):
  def test_empty_list(self):
    d =DoublyLinkedList(None)
    d.head =None
    d.tail =None
    d.length =0


    d.reverse()
    self.assertEqual( d.length, 0 )
    self.assertIsNone( d.head)


  def test_case_length_eq_1(self):
    d =DoublyLinkedList(0)
    d.reverse()
    self.assertEqual( d.head.value, 0 )
    self.assertIsNotNone( d.head)
    self.assertIsNotNone( d.tail)

  def test_case_length_eq_2(self):
    d =DoublyLinkedList(0)
    d.append(1)
    head_orig =d.head
    tail_orig =d.tail

    d.reverse()

    self.assertEqual( d.head.value, 1 )
    self.assertEqual( d.tail.value, 0 )
    self.assertIs( d.head , tail_orig)
    self.assertIs( d.tail , head_orig)


  def test_case_length_eq_5(self):
    d =DoublyLinkedList(0)
    d.append(1)
    d.append(2)
    d.append(3)
    d.append(4)
    head_orig =d.head
    tail_orig =d.tail

    d.reverse()

    self.assertEqual( d.head.value , 4)
    self.assertEqual( d.head.next.value , 3)
    self.assertEqual( d.head.next.next.value, 2)
    self.assertEqual( d.tail.prev.prev.value, 2)
    self.assertEqual( d.tail.prev.value , 1)
    self.assertEqual( d.tail.value , 0)

if __name__ == "__main__":
  unittest.main()