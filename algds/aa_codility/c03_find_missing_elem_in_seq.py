import sys

"""
python3 algds/aa_codility/c03_find_missing_elem_in_seq.py  2 3 5 6 4
// returns list_missing_element =[1]

"""
def find_missing_element_in_seq(seq):
  list_elem =[None]*(len(seq)+2)

  for elem in seq:
    try:
      list_elem[elem] =elem
    except IndexError:
      print("IndexError at elem={0}".format(elem))

  list_missing_element =[i for i in range(len(list_elem)) if list_elem[i] is None and i > 0]

  return list_missing_element




if __name__ == "__main__":
  list_int =[int(x) for x in sys.argv[1:]]
  list_missing_element =find_missing_element_in_seq(list_int)
  print('list_missing_element ={0}'.format(list_missing_element))
