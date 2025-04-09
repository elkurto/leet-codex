import sys
from collections import defaultdict

"""
@param: ary : a list of any type

@return - Return a list of values in :param:list that occur an odd number of times.

e.g.   find_unpaired_elements_in_list( [3,9,7,3,9,6] ) 
   // returns [7,6]
   
e.g.   find_unpaired_elements_in_list( [1,2,2, 10,10, 7,7,9,9,9, 4,4,4,4, 5,5,5,5,5] ) 
   // returns [1,9,5]     
"""
def find_unpaired_elements_in_list(ary):
  s =set()
  for element in ary:
    if element in s:
      s.remove(element)
    else:
      s.add(element)

  return list(s)


if __name__ == "__main__":
  #ary =[3,9,7,3,9,6]
  #ary_unpaired_element =find_unpaired_elements_in_list(ary)  # returns [7,6]
  ary_unpaired_element =find_unpaired_elements_in_list(sys.argv[1:])
  print( 'unpaired_elements ={0}'.format( ary_unpaired_element ))