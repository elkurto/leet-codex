import sys
from functools import reduce

"""
USAGE: 
  python3 algds/aa_codility/c03_find_min_abs_diff_between_two_partition.py 1 2 3 4 5
  min_diff =3  
  
  Compute min( abs_diff( sum(patition_a) - sum(partition_b))) 
  for all partition of :param:ary with rearrangement
  
  e.g. ary =[1,2,3,4,5]
    abs_diff     partition_a   partition_b
    |1-15|=14    1             2,3,4,5
    |3-12| =9    1,2             3,4,5 
    |6- 9| =3    1,2,3             4,5
    |10-5| =5    1,2,3,4             5
    Since min( 14, 9, 3, 5) = 3 
    ,then min_abs_diff_between_two_paritions = 3
       
   
"""

def find_min_abs_diff_between_two_partition(ary):
  sum_left =0
  sum_right = reduce(lambda x,y:x+y, ary, 0)
  min_abs_diff =abs(sum_left - sum_right)

  for p in range(1,len(ary)):
    sum_left +=ary[p-1]
    sum_right -=ary[p-1]

    min_abs_diff =min( abs(sum_left-sum_right ), min_abs_diff)

  return min_abs_diff

if __name__ == "__main__":
  list_int =[int(x) for x in sys.argv[1:]]
  min_diff =find_min_abs_diff_between_two_partition(list_int)
  print('min_diff ={0}'.format(min_diff))
