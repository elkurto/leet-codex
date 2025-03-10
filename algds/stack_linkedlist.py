class Node:
  def __init__(self, value):
    self.value =value
    self.next =None

class StackLinkedList:
  def __init__(self):
    self.top =None
    self.height =0

  def push(self, value):
    # same concept as LinkedList::push_first
    # ie. push new nodes to top (head) of stack
    node =Node(value)
    if not self.top:
      # empty list
      self.top =node
      self.height +=1
    else:
      # 1+ nodes
      node.next =self.top
      self.top =node
      self.height +=1

    return self

  def pop(self):
    # same concept as LinkedList::pop first
    # ie. pop nodes from top (head) of stack
    node =None

    if not self.top:
      # empty list
      pass
    else:
      # 1+ nodes in list
      node =self.top
      #  point top to second node
      self.top =self.top.next
      self.height -=1


    return node.value if node else None

  def values(self):
    list_value =[]
    curr =self.top
    while curr:
      list_value.append( curr.value )
      curr =curr.next()
    return list_value

  def __repr__(self):
    return "{0} : height={1}".format( self.values, self.height)

  def __str__(self):
    return self.__repr__()

