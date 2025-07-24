class StackFixedTypeAndSize:
  def __init__(self, clazz, maxlen=10):
    self.clazz =clazz
    self.maxlen =maxlen
    self.ary =[None]*maxlen
    self.population =0


  def append(self, element):
    if self.population >= self.maxlen:
      raise Exception(f"Exception idx ={idx} is invalid :: 0 <= idx < maxlen ({self.maxlen})")
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

  def __setitme__(self, idx, new_item):
    old_item =None
    if 0 <= idx < self.population:
      old_item =self.ary[idx] =new_item
    return old_item

  def pop(self, idx):
    item =None
    if 0 <= idx < self.population:
      item =self.ary.pop(idx)
      self.population -=1
    return item

