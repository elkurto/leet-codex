import sys

def fibonacci(n):
  slot_a =0
  slot_b =1

  if n <= 0 :
    return 0

  if not isinstance(n, int):
    return 0

  fibonacci_value =0
  for _ in range( 1, n):
    fibonacci_value = slot_a + slot_b
    slot_a =slot_b
    slot_b =fibonacci_value

  return fibonacci_value


if __name__ == "__main__":
  if len(sys.argv) >= 2:
    n =int( sys.argv[1] )
    fibonacci_value =fibonacci(n)
    print("n ={0} fibonacci_value ={1}".format(n, fibonacci_value))
  else:
    usage ="""
USAGE: 
  - python3 algds/fibbonacci_iterative.py <n>
  - Computes the nth fibbonacci number via iterative algorithm 
    (in O(n) linear compute complexity and O(2) space complexity).
  - e.g.     
      python3 algds/fibbonacci_iterative.py 5
      // prints the fifth fibonacci value
      // OUTPUT: n =5 fibonacci_value =8
    """
    print(usage)
    
"""

(venv) $ python3 algds/fibonacci_iterative.py 0
n =0 fibonacci_value =0

(venv) $ python3 algds/fibonacci_iterative.py 1
n =1 fibonacci_value =1

(venv) $ python3 algds/fibonacci_iterative.py 2
n =2 fibonacci_value =1

(venv) $ python3 algds/fibonacci_iterative.py 3
n =3 fibonacci_value =2

(venv) $ python3 algds/fibonacci_iterative.py 4
n =4 fibonacci_value =3

(venv) $ python3 algds/fibonacci_iterative.py 5
n =5 fibonacci_value =5

(venv) $ python3 algds/fibonacci_iterative.py 6
n =6 fibonacci_value =8

"""    