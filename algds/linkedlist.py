

class NodeLL:
  def __init__(self, value=None):
    self.value =value
    self.next =None


class LinkedList:
  def __init__(self):
    self.head =None
    self.tail =None
    self._size =0

  @classmethod
  def ensure_node(cls, value):
    if type(value) == NodeLL:
      node =value
    else:
      node =NodeLL(value)
    return node

  def push(self, value):
    newnode =self.ensure_node(value)

    if not self.head:
      # empty so add first node
      self.head =newnode
      self.tail =newnode
      self._size =1
    else:
      # non-empty so add second or more node
      self.tail.next =newnode
      self.tail =newnode
      self._size +=1

    return newnode.value

  def pop(self ):
    node =None
    if not self.tail:
      # empty
      pass
    elif self.tail == self.head:
      # 1 node only
      node =self.tail
      self.head =None
      self.tail =None
      self._size =0
    else:
      # 2+ nodes
      newtail =self.head
      while newtail.next != self.tail:
        newtail =newtail.next
      node =self.tail
      self.tail =newtail
      self.tail.next =None
      self._size -=1

    return node.value if node else None

  def size(self):
    return self._size

  def for_each(self, fn):

    curr =self.head
    i =0
    while curr is not None:
      fn( curr, i, self )
      curr =curr.next
      i +=1

  def print_all(self):
    fn =lambda n,i,llist:print( "{0} : {1}".format( i, n.value))
    self.for_each( fn )

  def pop_first(self):
    node =None

    if not self.head:
      # empty list
      pass
    else:
      # 1+ nodes in list
      node =self.head
      # head points to second node
      self.head =self.head.next
      self._size -=1

      # if empty, then nullify tail point too
      if node == self.tail:
        self.tail =None

    return node.value if node else None

  def push_all(self, *args):
    for arg in args:
      self.push(arg)

  def push_first(self, value):
    node =self.ensure_node(value)
    if not self.head:
      # empty list
      self.push( node )
      self._size +=1
    else:
      # 1+ nodes
      node.next =self.head
      self.head =node
      self._size +=1

    return value

  def _get_node_at_index(self, index):
    target_node =None
    curr_node =self.head

    if 0 <= index < self._size:

      i =-1
      while curr_node is not None :
        i+=1
        if i == index:
          target_node =curr_node
          break
        else:
          curr_node =curr_node.next

    return target_node

  def get_value_at_index(self, index):
    target_node =self._get_node_at_index(index)
    return target_node.value if target_node else None

  def at(self, index):
    return self.get_value_at_index(index)

  def set_value_at_index(self, value, index ):

    if index == self._size:
      # push to end of list
      self.push(value)
    else:
      target_node = self._get_node_at_index(index)
      if target_node is not None:
        target_node.value =value
      else:
        errmsg ="index={0} out of bounds.  index must be in [0, {1}]".format(index, self._size)
        raise IndexError(errmsg)

    return True


  def insert_value_at_index(self, value, index):

      if index == self._size:
        # case: insert new tail
        #  so push to end of list
        self.push(value)
      elif 0 == index:
        # case: insert new head
        #   so push_first to start of list
        self.push_first(value)

      elif 0 < index < self._size:
        # case: insert in middle
        #  a. acquire nodes at index and before index
        node_before_target =self._get_node_at_index(index-1)
        node_after_target =node_before_target.next
        # b. create the new node
        new_node =NodeLL(value)

        # c. adjust pointers and size
        node_before_target.next =new_node
        new_node.next =node_after_target
        self._size +=1

        # conditionally adjust tail pointer
        if node_before_target == self.tail:
          self.tail =new_node

      else:
        # index out of bounds
        errmsg ="index={0} out of bounds.  index must be in [0, {1}]".format(index, self._size)
        raise IndexError(errmsg)

      return True









