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
MAX_KEY =3 # max keys per node

class Rel(Enum):
  LT =0
  EQ =1
  GT =2

class Node234:

  def __init__(self, key=None, data=None, *children):
    self.keys =stack_fixed_size.StackFixedSize(MAX_KEY)  # any # non-None
    self.data =stack_fixed_size.StackFixedSize(MAX_KEY)   # any # possibly None -- # @todo handle multiple data at same key (ie make data a list)
    self.children =stack_fixed_size.StackFixedSize(MAX_KEY + 1)  # elements must be type, Node234

    if key is not None:
      self.keys.append(key)
      self.data.append(data)

    for child in children:
      if isinstance(child, Node234):
        self.children.append(child)
      else:
        break # ignore child children if child is None or wrong type

  def is_valid_or_raise(self):
    are_all_children_correct_type =reduce( lambda x,y : x and isinstance(y, type(self)), self.children[0:self.nchild()], True)
    if not are_all_children_correct_type:
      raise TypeError("all children must be type Node234")
    if len(self.children) >= MAX_KEY: # Check number of children
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
        relation =Rel.EQ
        break
      elif target < self.keys[i]:
        relation =Rel.LT
        break
      else:
        i +=1

    if i >= len(self.keys):
      relation =Rel.GT
    # return 0  if target <= keys[0]
    # return 1  if keys[0] < target <= keys[1]
    # return 2  if keys[1] < target <= keys[2]
    # return 3  if keys[2] < target
    return i, relation


  def is_empty(self):
    return len(self.keys) == 0

  def is_full(self):
    return len(self.keys) >= MAX_KEY

  def is_not_full(self):
    return len(self.keys) < MAX_KEY

  def insert_key_value(self, new_key, new_data, new_child=None):
    """
     case: new_key not in self.keys
      1. before: keys=[ a , c]
      2. call node.insert_key_value( 'b', 'bbbb')
      3. after: keys=[ a, b, c]

    """
    if self.keys.is_full():
      raise Exception(f"cannot insert key={new_key} into full node {str(self)}")

    # 1. find insertion index, i
    #   so find min(i) in {0,1,..MAX_KEY} where ( newKey <= key[i] or key[i] is None)
    i =0
    while i < MAX_KEY and i < len(self.keys) and self.keys[i] < new_key :
      i +=1


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
    if new_child:
      self.children.insert_at(i+1, new_child)

    return b_new_key

  def __str__(self):
    return f"<Node234_({'_'.join([str(k) for k in self.keys])})"

  def pop_key_data(self, idx=None):
    key =self.keys.pop(idx)
    data =self.data.pop(idx)
    return key,data

  def split_full_node(self):
    """

    :return: Node234 : new_right_node with keys[2],data[2],children[2:3]
    """
    if not self.is_full():
      raise Exception( f"Exception: attempting to split non-full node, len(node_to_split.keys) ={self.nkey()}")
    new_right_node =Node234( self.keys.pop(), self.data.pop(), *self.children[2:3])
    if len(self.children) >= 3:
      self.children.pop() # remove self.children[3]
    if len(self.children) >= 2:
      self.children.pop() # remove self.children[2]

    return new_right_node

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

  def find(self, target):
    return self.find_node_with_key(target)

  def find_node_with_key(self, target, curr=None):

    curr =self.root if curr is None else curr
    index,relation =curr.find_min_index_where_target_le_keys_elem(target)
    if relation == Rel.EQ:
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
    if self.root is None:
      self.root =Node234(key, data)
      self.population +=1
    else:
      self.__find_location_and_insert(key, data, self.root, self)

  def __find_location_and_insert(self, target_key, data, curr, parent):
    if curr is None:
      return curr, parent

    # a. split full nodes encountered during descent.
    # b. descend to find a leaf node (or node with exact key) for insertion

    # split full node before descent and before insert
    if curr.is_full():
      curr, parent =self.__split_node( curr, parent, target_key)
      # continue search at curr (which is orig curr or right sibling

    index,relation =curr.find_min_index_where_target_le_keys_elem(target_key)
    if relation == Rel.EQ:  # case: exact match
      curr.data[index] =data   #  replace data at key
      return curr,parent     #  stop
    else: #then not equal
      # if curr is a leaf, then insert
      if curr.is_leaf():
        curr.insert_key_value( target_key, data)
        self.population +=1
        return curr,parent  # stop
      else:
        # else keep searching recursively
        curr,parent =self.__find_location_and_insert(target_key, data, curr.children[index], curr)
        return curr,parent

  def __split_node(self, node_to_split, parent_node, target_key ):
    ### let node_to_split.keys= [40,50,60]

    new_node =node_to_split.split_full_node()
    # node_to_split.keys =[40,50]
    # new_node.keys =[60]

    key_middle,data_middle =node_to_split.pop_key_data()
    if parent_node is self:
      # then splitting root node, so create a new root/parent , and attach *children
      self.root =Node234( key_middle, data_middle, node_to_split, new_node)
      parent_node =self.root
      # new_root.keys =[50]
      # new_root.children[0] =node_to_split    (and node_to_split.keys =[40])
      # new_root.children[1] =new_node         (and new_node.keys =[60])

    else:
      # In parent_node exists, shift  keys[2],data[2],children[2]
      #   to right regardless if keys[2] is None.
      parent_node.insert_key_value( key_middle, data_middle, new_node )
      # parent_node.keys =[50]
      # parent_node.children[0] =node_to_split    (and node_to_split.keys =[40])
      # parent_node.children[1] =new_node         (and new_node.keys =[60])


    if target_key < key_middle:
      # then continue the search to the *left*
      rval_node =node_to_split
    else: # key_middle < target_key
      # then continue the search to the *right*
      rval_node =new_node

    return rval_node, parent_node

  def traverse_pre_order(self, fn_visit):
    self.__traverse_pre_order(fn_visit, self.root)

  def __traverse_pre_order(self, fn_visit, curr):
    if curr is None:
      return

    for i in range(0, curr.nkey()):
      # process subtree less than curr.key[i]
      if curr.children[i]:
        self.__traverse_pre_order(fn_visit, curr.children[i])

      # process curr.key[i]
      fn_visit( curr.keys[i])
    #end-for-i

    # process subtree greater than curr.key[2]
    if curr.children[3]:
      self.__traverse_pre_order(fn_visit, curr.children[3])

  def traverse_in_order(self, fn_visit):
    # traverse from top down
    self.__traverse_in_order( fn_visit, self.root)

  def __traverse_in_order(self, fn_visit, curr):
    curr_stack =[curr]
    child_stack =[]
    while len(curr_stack) > 0 or len(child_stack) > 0:
      # process one node
      ### pop from curr_stack
      node =curr_stack.pop()
      ### visit node
      fn_visit(node, curr_stack, child_stack)
      ### accumulate node's immediate children
      for child in reversed( node.children[0:3] ):
        if child:
          child_stack.append(child)

      if len(curr_stack) == 0:
        # then move to next level deep and continue processing
        curr_stack =child_stack
        child_stack =[]



  def remove(self, key):
    pass






