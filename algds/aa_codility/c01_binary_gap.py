import sys

"""
Binary Gap -
Given a decimal number's binary-representation
In  a binary number - determine the longest string of 0's between 1's.

e.g. bin(9) = '0b1001'  --
   longest_string_length_of_0s( 9 ) # returns 2

e.g. bin(529) ='0b1000010001'
   longest_string_length_of_0s( 529 ) # returns 4

e.g. bin( 7 ) ='0b111'
   longest_string_length_of_0s( 7 ) # returns 0

e.g. bin( 0 ) = '0b0'
   longest_string_length_of_0s( 0 ) # returns 0

e.g. bin( 20 ) = '0b10100'
   longest_string_length_of_0s( 20 ) # returns 1


"""

def longest_binary_gap_of_zeros( N ):
  n =abs( int(N))
  strbinary =bin(n)[2:]

  len_max =0
  len_temp =0

  for c in strbinary:
    if c == '1':
      if len_temp > len_max:
        len_max =len_temp
      len_temp =0
    else: #c==0
      len_temp += 1

  return len_max


if __name__ == "__main__":
  for arg in sys.argv[1:]:
    try:
      N =int(arg)
      i_longest_binary_gap =longest_binary_gap_of_zeros(N)
      print( "longest_binary_gap_of_zeros( {0} ) ={1}".format( N, i_longest_binary_gap))
    except ValueError:
      print( "bad input : arg is not convertible to int {0}".format(arg))

"""
USAGE:
python3 algds/aa_codility/c01_binary_gap.py 7 529 5 20
longest_binary_gap_of_zeros( 7 ) =0
longest_binary_gap_of_zeros( 529 ) =4
longest_binary_gap_of_zeros( 5 ) =1
longest_binary_gap_of_zeros( 20 ) =1

"""