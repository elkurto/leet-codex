
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

class BalancedTree234:


  def __init__(self):
    self.root =None