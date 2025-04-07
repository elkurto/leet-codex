import sys
"""
USAGE: 
 python3 algds/aa_codility/c00_bin2dec.py 0b101
 // returns 5

  python3 algds/aa_codility/c00_bin2dec.py 0b1011
  // returns 11
11

"""
def bin2dec( s_binary ):
  """
  Convert a base2 int to base10 int
  - A long form of int( s_binary, 2)
  :param s_binary: string of 1's and 0's
  :return: int - a base10

  """
  i_sum =0
  # reverse iterate s_binary
  # stop on first char not in (0,1)
  for i, digit in enumerate( reversed( s_binary)):
    if digit in ('0','1'):
      i_sum +=(1*pow( 2, i) if digit == '1' else 0)
    else:
      break

  return i_sum



if __name__ == "__main__":
  if len(sys.argv) >= 2:
    print( bin2dec( sys.argv[1] ))
