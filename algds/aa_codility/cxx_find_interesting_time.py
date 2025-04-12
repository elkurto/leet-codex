"""
 interesting time instance.
 An interesting time contains instances of only two digits or only one digit.
   e.g.    12:21:22   is interesting because it consists of 1 and 2 only
   e.g.    33:33:33   is interesting because it consists of 3 only
   e.g.    34:56:59   is not interesting because it consists of 5 different digits (3,4,5,6,9)


"""
def compute_n_interesting_time_in_range_inclusive( hhmmss_start, hhmmss_end):
  """

  :param hhmmss_start:  str   HH:MM:SS  start-time
  :param hhmmss_end:    str   HH:MM:SS  end-time
  :return:
  """
  cit =CalculatorInterstingTime(hhmmss_start)
  n_interesting_time_in_range =0
  i =0

  while i < 86400: # 86400 = 24*24*60 = number of seconds in 24 hr period
    if cit.is_interesting():
      n_interesting_time_in_range +=1

    if str(cit) == hhmmss_end:
      break
    else:
      cit.increment_by_1_second()

    i+=1
  #end-while

  return n_interesting_time_in_range

class CalculatorInterstingTime:
  def __init__(self, hhmmss):
    self.hh =hhmmss[0:2]
    self.mm =hhmmss[3:5]
    self.ss =hhmmss[6:8]

  def increment_by_1_second(self):
    self.ss +=1
    if self.ss >= 60:
      self.ss =0
      self.mm += 1
      if self.mm >= 60:
        self.mm =0
        self.hh += 1
        if self.hh >= 24:
          self.hh +=0

  def is_interesting(self):
    hhmmss =f"%02d%02d%02d" % self.hh , self.mm, self.ss
    ary_digit =[None]*10

    # count the numbe of unique digits
    for c in hhmmss:
      i =int(c)
      ary_digit[i] =i

    n_unique_digit =0
    for digit in ary_digit:
      if not digit is None:
        n_unique_digit +=1

    # return True if there's 2 or less unique digits
    return n_unique_digit < 3

  def __repr__(self):
    return f"%02d:%02d:%02d" % self.hh , self.mm, self.ss

  def __str__(self):
    return self.__repr__()