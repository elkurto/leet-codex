from functools import reduce
from enum import Enum
from balanced_tree_234 import stack_fixed_size

"""
Invariant: Each tree level is always balanced 
   Balance mean that each branch at same level has *equal height*.
   Balance does not imply that each subtree has equal content/population. 
Invariant: leaf-nodes can contain 1,2,3 keys
Invariant: non-leaf-nodes can contain 1 or two keys
Invariant: left keys < parent key
Invariant: right keys > parent key
Invariant: keys are unique
Invariant: only add to leaf nodes
Invariant: no 4 nodes (3key) at root) -- 2node(1key) and 3node(2key) allowed at root

"""
MAXKEY =3 # max keys per node

class Rel(Enum):
  NOT_EQUAL =0
  EQUAL =1

class Node234:

  def __init__(self, key=None, data=None, *children):
    self.keys =stack_fixed_size.StackFixedSize(MAXKEY)  # any # non-None
    self.data =stack_fixed_size.StackFixedSize(MAXKEY)   # any # possibly None -- # @todo handle multiple data at same key (ie make data a list)
    self.children =stack_fixed_size.StackFixedSize(MAXKEY+1)  # elements must be type, Node234

    if key is not None:
      self.keys.append(key)
      self.data.append(data)

    for child in children:
      self.children.append(child)

  def is_valid_or_raise(self):
    are_all_children_correct_type =reduce( lambda x,y : x and isinstance(y, type(self)), self.children[0:self.nchild()], True)
    if not are_all_children_correct_type:
      raise TypeError("all children must be type Node234")
    if len(self.children) >= MAXKEY: # Check number of children
      raise ValueError("2-3-4 nodes must be contain with 0,1,2,3 children")

    return True

  def is_leaf(self):
    return len(self.children) == 0

  def find_index_with_key_exact(self, key):
    i =0
    index_with_key =None
    while i < len(self.keys):
      if key == self.keys[i]:
        index_with_key =i
        break
      else:
        i +=1
    return index_with_key

  def find_min_index_where_target_le_keys_elem(self, target):
    i =0
    relation =None
    while i < len(self.keys):
      if target == self.keys[i]:
        # then found index
        relation =Rel.EQUAL
        break
      elif target < self.keys[i]:
        relation =Rel.NOT_EQUAL
        break
      else:
        i +=1

    # return 0  if target <= keys[0]
    # return 1  if keys[0] < target <= keys[1]
    # return 2  if keys[1] < target <= keys[2]
    # return 3  if keys[2] < target
    return i, relation


  def is_empty(self):
    return len(self.keys) == 0

  def is_full(self):
    return len(self.keys) >= MAXKEY

  def is_not_full(self):
    return len(self.keys) < MAXKEY

  def insert_key_value(self, new_key, new_data, *new_children):
    """
     case: new_key not in self.keys
      1. before: keys=[ a , c]
      2. call node.insert_key_value( 'b', 'bbbb')
      3. after: keys=[ a, b, c]

    """
    if self.keys.is_full():
      raise Exception(f"cannot insert key={new_key} into full node {str(self)}")

    # 1. find insertion index, i
    #   so find min(i) in {0,1,..MAXKEY} where ( newKey <= key[i] or key[i] is None)
    i =0
    while i < MAXKEY and i < len(self.keys) and new_key >= self.keys[i]:
      i +=1

    b_new_key =False
    if new_key == self.keys[i]:
      # 2. case: equal keys
      #    ,then replace data
      #    and ignore the subtree argument
      #    and return False (no new key)
      self.data[i] =new_data
      b_new_key = False # False indicates no new key added
    else:
      self.keys.insert_at(i, new_key)
      self.data.insert_at(i, new_data)
      b_new_key = True # return True to indicate a new key added

    # deal with *children
    # assume that there's no existing children
    # assume that not exists x such that child.keys[x] == new_key
    for child in new_children:
      if child.keys[i] < self.keys[i]:
        self.children.insert_at(i, child)
      elif child.keys[i] > self.keys[i]:
        self.children.insert_at(i+1, child)
      else:
        raise Exception( 'Exception: refusing to insert child.key == parent.key')

    return b_new_key

  def __str__(self):
    return f"<Node234_({'_'.join([str(k) for k in self.keys])})"

  def pop_key_data(self, idx=None):
    key =self.keys.pop(idx)
    data =self.data.pop(idx)
    return key,data

  def split_full_node(self):
    if not self.is_full():
      raise Exception( f"Exception: attempting to split non-full node, len(node_to_split.keys) ={self.nkey()}")
    new_right_node =Node234( self.keys.pop(), self.data.pop(), *self.children[2:3])
    if len(self.children) >= 3:
      self.children.pop() # remove self.children[3]
    if len(self.children) >= 2:
      self.children.pop() # remove self.children[2]

    return new_right_node


  def receive_left_key_from_child(self, key, data):
    self.keys.insert_at(0, key)
    self.data.insert_at(0, data)

  def receive_middle_key_from_child(self, key, data):
    self.keys.insert_at(1, key)
    self.data.insert_at(1, data)

  def receive_right_key_from_child(self, key, data):
    self.keys.insert_at(2, key)
    self.data.insert_at(2, data)



  def nkey(self):
    return len(self.keys)

  def ndata(self):
    return len(self.data)

  def nchild(self):
    return len(self.children)


class BalancedTree234:

  def __init__(self):
    self.root =None
    self.population =0

  def is_empty(self):
    return self.root is None

  def __find(self, goal_key, current_node, parent_node, b_split_full_nodes=True):
    pass

  def find(self, target):
    return self.find_node_with_key(target)

  def find_node_with_key(self, target, curr=None):

    curr =self.root if curr is None else curr
    index,relation =curr.find_min_index_where_target_le_keys_elem(target)
    if relation == Rel.EQUAL:
      return curr
    elif index < len(curr.children):
      # no exact match and children exist, then recurse through children
      curr =curr.children[index]
      if curr is not None:
        # recurse through children , then return result
        curr =self.find_node_with_key(target, curr)
    else:
      curr =None
    return curr

  def insert(self, key, data):
    self.__find_location_and_insert(key, data, self.root, self)

  def __find_location_and_insert(self, target_key, data, curr, parent):
    # a. split full nodes encountered during descent.
    # b. descend to find a leaf node (or node with exact key) for insertion



    # split full node before descent and before insert
    if curr.is_full():
      curr, parent =self.__split_node( curr, parent, target_key)
      # continue search at newNode

    index,relation =curr.find_min_index_where_target_le_keys_elem(target_key)
    if relation == Rel.EQUAL:  # case: exact match
      curr.data[index] =data   #  replace data at key
      return curr,parent     #  stop



    return curr,parent

  def __split_node(self, node_to_split, parent_node, target_key ):

    new_node =node_to_split.split_full_node()

    if parent_node is self:
      # then splitting root node, so create a new root/parent , and attach *children
      self.root =Node234( node_to_split.keys.pop(), node_to_split.data.pop(), node_to_split, new_node)

    else:
      # In parent_node exists, shift  keys[2],data[2],children[2]
      #   to right regardless if keys[2] is None.
      #
      parent_node.receive_middle_from_child( *node_to_split.pop_key_data() )




    if not node_to_split.is_leaf():

      nChild =len(node_to_split.children)
      new_node =Node234( node_to_split.keys[2], node_to_split.data[2], node_to_split.children[2:nChild])
      node_to_split.key.pop()
      node_to_split.data.pop()
      node_to_split.children.pop()

    if not node_to_split.is_leaf():
      # then move the children from node_to_split.children[2:3] to new_node[0:1]
      new_node.children[0] =node_to_split.children[2]
      new_node.children[1] =node_to_split.children[3]

    return node_to_split,parent_node

  def remove(self, key):
    pass



  def traverse(self, fnVisit):
    pass


