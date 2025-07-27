class StackFixedTypeAndSize:
  def __init__(self, clazz, maxlen=10):
    self.clazz =clazz
    self.maxlen =maxlen
    self.ary =[None]*maxlen
    self.population =0


  def append(self, element):
    if self.population >= self.maxlen:
      raise Exception(f"Exception fixed-sized-stack is full :: population={self.population} :: maxlen=({self.maxlen})")
    if not isinstance(element, self.clazz):
      raise Exception('element is not an instance of '+ self.clazz)

    self.ary[self.population] =element
    self.population +=1

  def __len__(self):
    return self.population

  def __iter__(self):
    return iter(self.ary)

  def __index__(self, idx):
    return self.ary[idx]

  def __getitem__(self, idx):
    return self.__index__(idx)

  def __setitem__(self, idx, new_item):
    return self.set_element_at_index(idx, new_item)

  def set_element_at_index(self, idx, new_item):
    old_item =None
    if 0 <= idx < self.population and idx < self.maxlen:
      # then replace existing element
      old_item =self.ary[idx]
      self.ary[idx] =new_item
    elif idx == self.population:
      self.append(new_item)
    else:
      raise IndexError( f"IndexError: idx={idx} must be in [0,population] == [0,{self.population} and idx < maxlen({self.maxlen})")

    return old_item

  def pop(self, idx=None):
    item =None
    if idx is None:
      idx =self.population -1  # compute last index

    if 0 <= idx < self.population: # remove item at last index
      item =self.ary.pop(idx)
      self.population -=1

    return item

  def push(self, element):
    return self.append(element)

