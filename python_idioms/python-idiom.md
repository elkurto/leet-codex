# Python Idioms


#### Array Comprehensions
##### goal: Double the values of elements in :list:a. 
  ```python
    a =[1,2,3,4,5]
    
    # 
    b =[ x*2 for x in a ]  

    print(b)
    # Output:
    # [2, 4, 6, 8, 10]
  ```

##### goal: Double the even values in :list:a (skip the odd values)
  ```python
    a =[1,2,3,4,5]
    b =[ x*2 for x in a if x % 2 == 0 ]
    print(b)
    
    # Output:
    # [4, 8]
``
    
  ```
