import sys

class FibonacciWithDynamicProgTopDown:
  def __init__(self):
    self.ary_fibonacci_number =[0,1]

  def fibonacci(self, n):
    if n <= 0:
      return 0
    elif not isinstance(n, int):
      return 0

    return self._fibonacci(n)

  def _fibonacci(self, n):
    if n < len(self.ary_fibonacci_number):
      return self.ary_fibonacci_number[n]
    else:
      fibonacci_value =self._fibonacci(n-2) + self._fibonacci(n-1)
      if n == len(self.ary_fibonacci_number):
        self.ary_fibonacci_number.append( fibonacci_value)
      return fibonacci_value


if __name__ == "__main__":
  if len(sys.argv) >= 2:
    n =int( sys.argv[1] )
    fib =FibonacciWithDynamicProgTopDown()
    fibonacci_value =fib.fibonacci(n)
    print("n ={0} fibonacci_value ={1}".format(n, fibonacci_value))
  else:
    usage ="""
USAGE: 
  - python3 algds/fibonacci_dynamic_prog_top_down.py <n>
  - Computes the nth fibbonacci number via top-down dynamic programming with memoization. 
    (in O(n) linear compute complexity and O(n) space complexity).
  - e.g.     
      python3 algds/fibbonacci_iterative.py 5
      // prints the fifth fibonacci value
      // OUTPUT: n =5 fibonacci_value =8
    """
    print(usage)
    
"""

(venv) kurt5@dingo5:alggraph$ for i in {0..6}; do python3 algds/fibonacci_dynamic_prog_top_down $i; done
n =0 fibonacci_value =0
n =1 fibonacci_value =1
n =2 fibonacci_value =1
n =3 fibonacci_value =2
n =4 fibonacci_value =3
n =5 fibonacci_value =5
n =6 fibonacci_value =8




"""    