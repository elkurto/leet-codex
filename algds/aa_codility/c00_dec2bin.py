import sys

"""
USAGE:
  python3 algds/aa_codility/c00_dec2bin.py 22
  // returns +10110

  python3 algds/aa_codility/c00_dec2bin.py 11
  // returns +1011

"""
def dec2bin( n ):
  """
  Convert a base10 int to base2 int
  This is a custom version of :builtin_function:"bin( n )"
  :param n: int a base10 integer
  :return: a stringified signed base2 representation of :param:n

  """

  dividend =abs(int( n ))
  sign ='+' if dividend >= 0 else '-'
  remainder =0
  result =[]

  if n == 0:
    result =[remainder]
  else:
    while True:

      (dividend,remainder) =divmod( dividend, 2)
      result.append(str(remainder))
      if dividend < 1:
        break

  result.reverse()
  return "{sign}{binstr}".format(sign=sign, binstr=''.join( result ))


if __name__ == "__main__":
  if len(sys.argv) >= 2:
    print( dec2bin( sys.argv[1] ))
