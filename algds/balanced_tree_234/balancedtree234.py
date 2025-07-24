
class Node234:
  def __init__(self, key=None, data=None, *children):
    self.nKey =0
    self.keys =[]  # any # non-None
    self.data =[]  # any
    self.children =children  # must be type = Node234
    self.nChildren =len(children)  # must have length in 0,1,2

    if key is not None:
      self.nKey =1
      self.keys.append(key)
      self.data.append(data)

  def is_valid(self):
    valid = [x for x in children # Extract valid child links
             if isinstance(x, type(self))]
    if len(valid) not in (0, 2): # Check number of children
      raise ValueError("2-3-4 nodes must be created with 0,1,or 2 children")

class BalancedTree234:

  def __init__(self):
    self.root =None