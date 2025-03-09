import unittest

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    

class LinkedList:
  def __init__(self, value):
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node

    
  def append(self, value):
    new_node = Node(value)
    if self.head == None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    return True
  
def find_kth_from_end(LL, k):
  
  a=LL.head
  b=LL.head

  if k < 0:
    return Node(None)
    
  # move b to kth node from a and from head
  for i in range(0,k):
    if b.next is None:
      return Node(None)
    b =b.next  
        
  # now b and a are k nodes apart.
  # so advance by a and b by one node
  #  until b == None, then return a.value
  while True:
    if b.next is None:
      return a
    b =b.next
    a =a.next


class Test(unittest.TestCase):

  def createLinkedList(self, *args):
    if len(args) == 0:
      raise Exception( "args must have one or more values -- no empty list")
    llist =LinkedList(args[0])

    if len(args) > 1:
      for arg in args[1:]:
        llist.append(arg)

    return llist
      

  def test_empty_list(self):
    llist =LinkedList(None)
    node =find_kth_from_end( llist,  0 )
    self.assertIsNone( node.value)

    node =find_kth_from_end( llist, 10)
    self.assertIsNone( node.value)

  def test_k_at_end(self):
    llist =self.createLinkedList(1,2,3,4)
    node =find_kth_from_end( llist, 0 )
    self.assertEqual( node.value, 4)

  def test_k_before_end(self):
    llist =self.createLinkedList(1,2,3,4)
    node =find_kth_from_end( llist, 1 )
    self.assertEqual( node.value, 3)

  def test_k_after_end(self):
    llist =self.createLinkedList(1,2,3,4)
    node =find_kth_from_end( llist, -1 )
    self.assertEqual( node.value, None)
  
if __name__ == "__main__":
  unittest.main()







