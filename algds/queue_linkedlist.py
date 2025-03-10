class Node:
  def __init__(self, value):
    self.value =value
    self.next =None
    self.prev =None

class QueueLinkedList:
  def __init__(self):
    self.head =None
    self.tail =None
    self.length =0


  def push(self,value):
    node =Node(value)
    # push to the head of the list
    if self.head is None:
      # case: empty list
      self.head =node
      self.tail =node

    else:
      # case: length >= 1
      new_node =Node(value)
      new_node.next =self.head
      self.head.prev =new_node
      self.head =new_node

    #increment length
    self.length +=1


  def pop(self):
    # pop from the tail of the list
    node_old_tail =None
    if self.tail:
      # case: non-emtpy list
      node_old_tail =self.tail

      # assign new tail
      self.tail =self.tail.prev

      # manage ptrs , head and tail
      if self.tail:
        # subcase length >= 1 , detach old tail
        self.tail.next =None

      if self.head == node_old_tail:
        # subcase  initial_length == 1 , so empty the list
        self.head =None

      # detach old tail
      node_old_tail.prev =None

      # decrement length
      self.length -=1
    #end-if

    return node_old_tail.value if node_old_tail else None

  def values(self):
    list_value =[]
    curr =self.head
    while curr:
      list_value.append( curr.value )
      curr =curr.next()
    return list_value

  def __repr__(self):
    return "{0} : height={1}".format( self.values, self.length)

  def __str__(self):
    return self.__repr__()

