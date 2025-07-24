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

    self.population +=1
    self.ary[self.population] =element


  def __len__(self):
    return self.population

  def __iter__(self):
    return iter(self.ary)

  def __index__(self, idx):
    return self.ary[idx]
