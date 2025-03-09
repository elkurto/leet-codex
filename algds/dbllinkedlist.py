class Node:
  def __init__(self, value ):
    self.value =value
    self.next =None
    self.prev =None

class DoubleLinkedList:
  def __init__(self):
    self.head =None
    self.tail =None
    self.length =0

  def append_args( self, *args):
    for arg in args:
      self.append( arg )
    return self

  def values(self):
    list_values =[]
    curr =self.head
    while curr:
      list_values.append(curr.value)
      curr =curr.next

    return list_values
  

  def append(self, value):
    node =Node(value)
    if self.head is None:
      self.head =node
      self.tail =node
    else:
      self.tail.next =node
      node.prev =self.tail
      self.tail =node
    # increment length
    self.length +=1
  
  def pop(self):
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
        # subcase  length == 1 , so empty the list 
        self.head =None

      # detach old tail
      node_old_tail.prev =None

      # decrement length
      self.length -=1

    return node_old_tail.value if node_old_tail else None

  def prepend(self, value):


    if self.head is None:
      # case: empty list
      self.append( value )
    else:
      # case: length >= 1
      new_node =Node(value)
      new_node.next =self.head
      self.head.prev =new_node
      self.head =new_node
      self.length +=1
    

  def pop_first(self):
    old_head =self.head

    # case length >= 1
    if old_head:
      old_head =self.head

      # detach old_head replace with new_head
      self.head =self.head.next
      old_head.next =None

      if self.head is None:
        # subcase original_length == 1
        # so nullify tail too (to empty the list)
        self.tail =None

      # decrement
      self.length -=1
    #end-if

    return old_head.value if old_head else None

  def _get_node_at_index(self, index):
    curr =None
    if 0 <= index < self.length:
      curr =self.head
      for i in range(0,index):
        curr =curr.next
    return curr

  def get(self, index):
    curr =self._get_node_at_index(index)
    return curr.value if curr else None

  def set(self, index, value):
    curr =self._get_node_at_index(index)
    if curr:
      curr.value =value

  def insert( self, index, value):
    if not( 0 <= index <= self.length):
      raise IndexError( "IndexError: index must be [0,{0}]; actual index ={1}".format( self.length, index))

    if index == 0:
      self.prepend(value)
    elif index == self.length:
      self.append( value )
    else:
      node_left =self._get_node_at_index(index-1)
      node_right =node_left.next
      node_new =Node(value)  #insertee

      if node_left:
        node_left.next =node_new
        node_new.prev =node_left

      if node_right:
        node_new.next =node_right
        node_right.prev =node_new
      # increment
      self.length +=1
    #end-if


  def remove( self, index ):

    # validate [0 <= index < length ] else raise IndexException
    if not( 0 <= index < self.length):
      raise IndexError( "IndexError: index must be [0,{0}]; actual index ={1}".format( self.length-1, index))

    node_at_index =None
    value =None
    # case empty : if length == 0 then return None (noop)
    ###
    if self.head and self.head.next is None:
      # if length == 1  then remove tail and head (just pop)
      value =self.pop()
    elif self.head:
      # if valid index and length >= 2
      # then decouple node_at_index and return value
      node_at_index =self._get_node_at_index(index)
      node_left =node_at_index.prev
      node_right =node_at_index.next

      node_at_index.prev =None
      node_at_index.next =None

      if node_left:
        node_left.next =node_right

      if node_right:
        node_right.prev =node_left

      value =node_at_index.value
      self.length -= 1

    return value

  def __repr__(self):
    return self.__str__( )
  
  def __str__(self):
    head_val =self.head.value if self.head else None
    tail_val =self.tail.value if self.tail else None

    stringified_state ="list ={0}; len={1}; h={2}; t={3}".format( self.values(), self.length, head_val, tail_val )
    return stringified_state

