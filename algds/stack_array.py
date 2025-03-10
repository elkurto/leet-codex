class StackArray:
  def __init__(self):
    self.ary =list()

  def __len__(self):
    return len(self.ary)

  def size(self):
    return self.__len__()

  def push(self, value):
    self.ary.append(value)
    return self

  def pop(self):
    value =None
    if len(self.ary) > 0:
      value =self.ary.pop()
    return value

  def __repr__(self):
    return "{0} : length={1}".format( self.ary, self.size())

  def __str__(self):
    return self.__repr__()
