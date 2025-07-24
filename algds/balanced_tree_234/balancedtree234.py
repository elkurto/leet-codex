from functools import reduce

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
class Node234:
  def __init__(self, key=None, data=None, *children):
    self.keys =[]   # any # non-None
    self.data =[]   # any # possibly None -- # @todo handle multiple data at same key (ie make data a list)
    self.children =children  # must be type = Node234

    if key is not None:
      self.keys.append(key)
      self.data.append(data)

  def is_valid(self):
    are_all_children_correct_type =reduce( lambda x,y : x and isinstance(y, type(self)), self.children, True)

    if len(self.children) not in (0, 2): # Check number of children
      raise ValueError("2-3-4 nodes must be created with 0 or 2 children")

  def is_leaf(self):
    return len(self.children) == 0

  def __str__(self):
    return f"<Node234_({'_'.join([str(k) for k in self.keys])})"

  def
class BalancedTree234:

  def __init__(self):
    self.root =None