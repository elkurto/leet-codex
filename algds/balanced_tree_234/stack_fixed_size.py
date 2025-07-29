class StackFixedSize:
  def __init__(self, maxlen=10):
    self.__maxlen =maxlen
    self.__ary =[None]*maxlen
    self.__population =0

  def capacity(self):
    return self.__maxlen

  def size(self):
    return self.__population

  def append(self, element):
    if self.__population >= self.__maxlen:
      raise IndexError(f"Exception fixed-sized-stack is full :: __population={self.__population} :: maxlen=({self.__maxlen})")

    self.__ary[self.__population] =element
    self.__population +=1

  def push(self, element):
    return self.append(element)

  def __len__(self):
    return self.__population

  def __iter__(self):
    return iter(self.__ary)

  def __index__(self, idx):
    return self.__ary[idx]

  def __getitem__(self, idx):
    return self.__index__(idx)

  def __setitem__(self, idx, new_item):
    return self.set_element_at_index(idx, new_item)

  def set_element_at_index(self, idx, new_item):
    old_item =None
    if 0 <= idx < self.__population and idx < self.__maxlen:
      # then replace existing element
      old_item =self.__ary[idx]
      self.__ary[idx] =new_item
    elif idx == self.__population:
      self.append(new_item)
    else:
      raise IndexError( f"IndexError: idx={idx} must be in [0,__population] == [0,{self.__population} and idx < maxlen({self.__maxlen})")

    return old_item

  def pop(self, idx=None):
    item =None
    if idx is None:
      idx =self.__population -1  # compute last index

    if 0 <= idx < self.__population: # remove item at last index
      item =self.__ary.pop(idx)
      self.__population -=1

    return item


