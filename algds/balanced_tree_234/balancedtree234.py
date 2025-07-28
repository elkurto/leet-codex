from functools import reduce
from enum import Enum
from stack_fixed_type_size import StackFixedTypeAndSize
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
    self.keys =[]  # any # non-None
    self.data =[]   # any # possibly None -- # @todo handle multiple data at same key (ie make data a list)
    self.children =children  # must be type = Node234

    if key is not None:
      self.keys.append(key)
      self.data.append(data)

  def is_valid(self):
    are_all_children_correct_type =reduce( lambda x,y : x and isinstance(y, type(self)), self.children, True)

    if len(self.children) >= MAXKEY: # Check number of children
      raise ValueError("2-3-4 nodes must be created with 0 or 2 children")

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

  def insert_key_value(self, new_key, new_data, new_subtree):
    # 1. find insertion index, i
    #   so find min(i) in (0,1,2) where ( newKey <= key[i] or key[i] is None)
    i =0
    while i < MAXKEY and new_key <= self.keys[i] :
      i +=1

    if i >= MAXKEY:
      raise Exception(f"cannot insert key={new_key} into full node {str(self)}")

    if new_key == self.keys[i]:
      # 2. case: equal keys
      #    ,then replace data
      #    and ignore the subtree argument
      #    and return False (no new key)
      self.data[i] =new_data
      return False
    else:
      j =len(self.keys)
      if j >= MAXKEY:
        raise Exception(f"cannot insert key={new_key} into full node {str(self)}")

      # 2.1. case: insert fresh newKey, newData, and newSubtree
      #   ,then make a hole at index, i,  by shifting all to right
      #   ,then assign newKey, newData, and newSubtree at index,i
      while i < j:
        self.keys[j] =self.keys[j-1]
        self.data[j] =self.data[j-1]
        self.children =self.children[j-1]
        j -=1
      #end-while

      self.keys[i] =new_key
      self.data[i] =new_data
      if new_subtree:
        self.children[i] =new_subtree
      else:
        self.children[i] =None
      return True

  def __str__(self):
    return f"<Node234_({'_'.join([str(k) for k in self.keys])})"


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

    if node_to_split.is_leaf()
      new_node =Node234( node_to_split.keys[2], node_to_split.data[2])
    else:
      nChild =len(node_to_split.children)
      new_node =Node234( node_to_split.keys[2], node_to_split.data[2], node_to_split.children[2:nChild])
      node_to_split.key.pop()
      node_to_split.data.pop()
      node_to_split.children.pop()

    if not node_to_split.is_leaf():
      # then move the children from node_to_split.children[2:3] to new_node[0:1]
      new_node.children[0] =node_to_split.children[2]
      new_node.children[1] =node_to_split.children[3]



  def remove(self, key):
    pass



  def traverse(self, fnVisit):
    pass


