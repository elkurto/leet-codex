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

  def is_two_node(self):
    return len(self.keys) == 1

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

  def replace_key_data_at_i(self, key_replacer, data_replacer, i):
    key_replaced =self.keys[i]
    data_replaced =self.data[i]

    self.keys[i] =key_replacer
    self.data[i] =data_replacer

    return key_replaced, data_replaced


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

  def to_csv_keys(self):
    return ",".join( [str(k) for k in self.keys])


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

  def _find_node_with_exact_key_and_prep_for_remove(self, target, curr, parent=None):
    # return
    #   if target key exist
    #   ,then return curr_node, parent_node, idx_of_key (in curr_node)
    #   else # target does not exist
    #   ,then return None,None,None
    #
    if curr is None:
      return None,None,None

    i =self.compute_idx_idiom(target, curr)
    if i < curr.nkey() and target == curr.keys[i]:
      return curr, parent, i
    elif curr.is_leaf():
      return None,None,None

    # note: i is the index in curr.children to travel nextly.
    # note: j is the index in curr.keys that attaches to curr.children[i]
    # (ie curr.children[i] is the subtree to search nextly)
    # (ie curr.keys[j] is the parent key of curr.children[i])
    # (ie curr.children[i] is the right or the left child of curr.keys[j])
    j =i if i < curr.nkey() else i-1

    if curr.children[j].is_two_node() and curr.children[j+1].is_two_node():
      #, then fuse curr.key[j], children[j] and children[j+1] into children[j]
      curr,parent,j =self.do_fusion_left( curr, parent, j)
      return self._find_node_with_exact_key_and_prep_for_remove(target, curr, parent)
    elif curr.children[i].is_two_node():
      # then child to travel is a 2node and sibling is 3node or 4node
      #  so rotate from fuller sibling to curr.children[i] (ie node to visit nextly)
      if i == j:
        # then rotate left from curr.children[i+1]
        # and rotate down curr.key[i] into curr.children[i]
        self._rotate_left(curr, j )
      else: # i-1 = j
        # then rotate right from curr.children[i-1]
        # and rotate down curr.key[i] into curr.children[i]
        self._rotate_right(curr, j )
      # recursively continue to descend
      return self._find_node_with_exact_key_and_prep_for_remove(target, curr.children[i], curr)
    else:
      # then curr.children[i] is a 3node or 4node
      # recursively continue to descend (and no need to modify curr.children[i]
      return self._find_node_with_exact_key_and_prep_for_remove(target, curr.children[i], curr)






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
      for child in reversed( node.children[0:4] ):
        if child:
          child_stack.append(child)

      if len(curr_stack) == 0:
        # then move to next level deep and continue processing
        curr_stack =child_stack
        child_stack =[]

  def print_tree(self):
    ary =[""]
    def fn_print_node(node, curr_stack, child_stack):
      ary[len(ary)-1] += node.to_csv_keys()
      if len(curr_stack) == 0:
        ary[len(ary)-1] +="|"
        ary.append("")
      else:
        ary[len(ary)-1] +="  "

    self.traverse_in_order(fn_print_node)

    for elem in ary:
      print(elem)

  def _find_idx_of_curr_node_in_parent_children(self, curr, parent):
    if parent is None or curr is None:
      return None

    idx_rval =None
    i =0
    while i < parent.nchild():
      if curr is parent.children[i]:
        idx_rval =i
        break
      else:
        i +=1
    #end-while
    return idx_rval

  def do_fusion_left(self, curr, parent, i):
    # pre: children[i] and children[i+1] are both two-nodes
    # post: fused parent.keys[i], children[i+1].keys[0], children[i].key[0] into :node:children[i]
    # return: :Node234: left (aka children[i])
    left =curr.children[i]                # make some dummy vars
    right =curr.children[i+1]

    curr_key, curr_data =curr.pop_key_data(i)
    left.keys[1] =curr_key                # move key and data from curr to left
    left.data[1] =curr_data

    left.keys[2] =right.keys[0]           # move key and data from right to left
    left.data[2] =right.data[0]

    if not right.is_leaf():
      left.children[2] =right.children[0]   # move children from right to left
      left.children[3] =right.children[1]

    curr.children.pop( i+1 )              # remove right from curr

    new_parent =curr
    if curr.nkey() == 0:
      idx_of_curr_in_parent_children =self._find_idx_of_curr_node_in_parent_children(curr, parent)
      parent.children[idx_of_curr_in_parent_children] =left
      new_parent =parent
    return left, new_parent, 1

  def contains(self, target):
    return self._contains(target, self.root)

  def _contains(self, target, curr):
    if curr is None:
      return False
    i =self.compute_idx_idiom(target, curr)

    if i < curr.nkey() and target == curr.keys[i]:
      # then found target
      return True
    else:
      # then not found target so keep searching recursively
      return self._contains( target, curr.children[i])

  def compute_idx_idiom(self, target, curr):
    i =0
    while i < curr.nkey() and target > curr.keys[i]:
      i+=1
    return i

  def remove(self, target):
    """
    :param target: the key to find and remove
    :return:  key,data  - if some key === target
        None,None - if there exists no key === target
    :post-condition: key,data removed from tree
    """
    if target is None:
      return None,None
    if self.root is None:
      return None,None
    # if not self.contains(target):
    #   return None,None


    # if self.root.is_leaf():
    #   i =self.compute_idx_idiom(target, self.root)
    #   if i < self.root.nkey() and target == self.root.keys[i]:
    #     return self.root.pop_key_data(i)
    #   else:
    #     return None,None
    #
    # elif self.root.is_two_node():
    #   if self.root.children[0].is_two_node() and self.root.children[1].is_two_node():
    #     #, then fuse root, children[0] and children[1] into children[0]
    #     self.root =self.do_fusion_left( self.root, None, 0)

    return self._remove(target, self.root, None, i=None)



  def _remove(self, target, curr, parent, i=None):

    """
    1. find *target_node* and *idx_in_target_node* with b_prepare =True
    2. replace target_node.keys[idx_in_target_node] with predecessor
    2.a find predecessor (max key in subtree target_node.children[idx_in_target_node]) with b_prepare=True
    2.b at target_node.keys[idx_in_target_node], remove target key,date and replace with predecessor
    or
    3. replace target_node.keys[idx_in_target_node] with successor
    """
    if i is None:
      curr,parent,i =self._find_node_with_exact_key_and_prep_for_remove(target, curr, parent)

    if curr is None:
      # then target does not exist
      return None,None

    if curr.is_leaf():
      if i < curr.nkey():
        # then target exists in leaf
        key,data =curr.pop_key_data( i )
        return key,data
      else:
        # then target does not exist
        return None,None

    # now find successor or predecessor, then swap out target_key and target_data.
    if curr.children[i].is_two_node() and curr.children[i+1].is_two_node():
      curr,parent,i =self.do_fusion_left(curr,parent,i)
      # note: fusion move the target key so
      return self._remove(target, curr, parent, i)

    elif curr.children[i].is_two_node():
      # then curr.children[i+1] is a three node or four node
      #  so replace curr.keys[i] and curr.data[i] with key_successor and data_successor
      key_successor,data_successor =self._delete_min_in_subtree(curr.children[i+1], curr )
      key,data =curr.replace_key_data_at_i( key_successor,data_successor, i)

    else: # then curr.children[i+1].is_two_node():
      # then curr.children[i] is a three node or four node
      #  so replace curr.keys[i] and curr.data[i] with key_predecessor and data_predecessor
      key_predecessor,data_predecessor =self._delete_max_in_subtree(curr.children[i], curr )
      key,data =curr.replace_key_data_at_i( key_predecessor,data_predecessor, i )


    return key,data

  def _delete_min_in_subtree(self, curr, parent):
    # pre: curr is not a two_node
    if curr.is_two_node():
      raise Exception('Exception: precondition violation ::: curr must be a three_node or four_node')

    if curr.is_leaf():
      key_min,data_min =curr.pop_key_data(0)
      return key_min,data_min
    else:
      if curr.children[0].is_two_node() and curr.children[1].is_two_node():
        # ensure that curr.children[0] is not a two node
        curr,parent,_ =self.do_fusion_left(curr, parent, 0)
        return self._delete_min_in_subtree(curr, parent)
      elif curr.children[0].is_two_node():
        # ensure that curr.children[0] is not a two node
        self._rotate_left( curr, 0)
      return self._delete_min_in_subtree(curr.children[0], curr)

  def _rotate_left(self, curr, i):
    # :param: curr :Node234 -
    # :param: i :int - i indicates the intent to rotate-left-down curr.keys[i]
    """
                        rotate_left(curr,i=0) -->
    curr= [25, 50,..]                        curr= [30,50,...]
          /   |                                    /   /
       [4]   [30,35,..] [...] [...]          [4,25]  [35,..] [...] [...]
      /  |    |  ...                        /  |  |    ...
   s4.0 s4.1 s30.0 ...                  s4.0 s4.1 s30.0 ...

    note: s4.0, s4.1, and s30.0 represent children (subtree or None)
    """
    left =curr.children[i]
    right =curr.children[i+1]

    # remove min key,data,child from :node:right
    min_key_right, min_data_right =right.pop_key_data( 0)

    min_right_child =None if right.is_leaf() else right.children.pop(0)

    # replace curr.keys[i] and curr.data[i]
    key_i,data_i =curr.replace_key_data_at_i(min_key_right, min_data_right, i)

    # left node receives
    left.insert_key_value( key_i, data_i, min_right_child)


  def _delete_max_in_subtree(self, curr, parent):
    # pre: curr is not a two_node
    # pre: Let i =curr.nkey()-1 ;
    #      either curr.children[i] and curr.children[i+1] both exist
    #      or curr is leaf.
    if curr.is_two_node():
      raise Exception('Exception: precondition violation ::: curr must be a three_node or four_node')

    i =curr.nkey() -1
    if curr.is_leaf():
      key_max,data_max =curr.pop_key_data(i)
      return key_max,data_max
    else:
      if curr.children[i].is_two_node() and curr.children[i+1].is_two_node():
        # then fuse to ensure that curr.children[0] is not a two node
        curr,parent,_ =self.do_fusion_left(curr, parent, i-1)
        return self._delete_max_in_subtree(curr, parent)
      elif curr.children[i+1].is_two_node():
        # then rotate_right to ensure that curr.children[0] is not a two node
        self._rotate_right( curr, i)
      return self._delete_max_in_subtree(curr.children[i+1], curr)

  def _rotate_right(self, curr, i):
    # pre: curr.children[i] and curr.children[i+1] exist
    # @param i is the index in curr.keys to rotate (rightward and downward)
    #
    """

                          rotate_right(curr,i=nkey-1) -->
      curr= [...  ,30   , ...   ]        curr= [...,25 , ...]
                 /      \                          /   \
         [..,4,25]       [50  ]               [..,4]    [30  ,  50]
        ..  / |  \        |   \                 /  |    |    |    \
    ..  s4.0 s4.1 s25.0  s50.0 s50.1        s4.0 s4.1  s25.0 s50.0 s50.1

      note: s4.0, s4.1, s25.0, s50.0, s50.1 represent children (subtree or None)
    """
    left =curr.children[i]
    right =curr.chldren[i+1]

    # remove min key,data,child from :node:right
    idx_keys_left =left.nkey()-1
    max_key_left, max_data_left =left.pop_key_data( idx_keys_left)
    max_left_child =left.children.pop(idx_keys_left+1)

    # replace curr.keys[i] and curr.data[i]
    key_i,data_i =curr.replace_key_data_at_i( max_key_left, max_data_left, i)

    # left node receives
    right.insert_key_value( key_i, data_i, max_left_child)
















