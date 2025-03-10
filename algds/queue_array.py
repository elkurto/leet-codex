
class QueueArray:
  """
  A queue implementation backed by an array instead of a linkedlist
  """
  def __init__(self):
    self.ary =[]

  def __len__(self):
    return len(self.ary)

  def size(self):
    return self.__len__()

  def push(self, value):
    # push new values to front
    self.ary.insert( 0, value)
    return self

  def pop(self):
    # pop values from tail
    value =None
    if len(self.ary) > 0:
      value =self.ary.pop()
    return value

  def is_empty(self):
    return self.size() < 1

  def peek(self):
    peek_value =None
    if not self.empty:
      peek_value =self.ary[-1]
    return peek_value

  def __repr__(self):
    return "{0} : length={1}".format( self.ary, self.size())

  def __str__(self):
    return self.__repr__()
