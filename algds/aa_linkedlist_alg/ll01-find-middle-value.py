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

  def find_middle_node(self ):
    a =self.head
    b =self.head

    while True:
      if b is None or b.next is None:
        return a
      else:
        a =a.next
        b =b.next.next
