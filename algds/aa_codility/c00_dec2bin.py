import sys

def dec2bin( n ):
  """
  Convert a base10 int to base2 int
  :param n: int
  :return:
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
