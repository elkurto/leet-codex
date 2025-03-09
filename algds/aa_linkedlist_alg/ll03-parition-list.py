class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self, value):
    new_node = Node(value)
    self.head = new_node
    self.length = 1

  def append(self, value):
    new_node = Node(value)
    if self.length == 0:
      self.head = new_node
    else:
      current_node = self.head
      while current_node.next is not None:
        current_node = current_node.next
      current_node.next = new_node
    self.length += 1

  def print_list(self):
    temp = self.head
    while temp is not None:
      print(temp.value)
      temp = temp.next

  def make_empty(self):
    self.head = None
    self.length = 0

  def get_tail_node(self):
    tail_node =self.head

    while tail_node and tail_node.next is not None:
      tail_node =tail_node.next

    return tail_node

  def append_linked_list(self, linked_list_tail):
    if linked_list_tail is None:
      #case: linked_list_tail is none so nothing todo
      pass
    else:

      if self.head is None:
        #case self is empty, so assign self.head
        self.head =linked_list_tail.head

      else:
        #case self is not empty, so find self.tail and self.tail = self.head
        tail_node =self.get_tail_node()
        tail_node.next =linked_list_tail.head


  def partition_list(self, partition_value):
      linked_list_lt =None #LinkedList(None)
      linked_list_gt =None #LinkedList(None)

      # 1. partition
      # for each node in self,
      #   IF node.value < partition_value THEN append Node(value) to linked_list_lt
      #   IF node.value >= partition_value THEN append Node(value) to linked_list_gt
      curr_node =self.head
      while curr_node is not None:
        if curr_node.value < partition_value:
          if linked_list_lt is None:
            linked_list_lt =LinkedList( curr_node.value )
          else:
            linked_list_lt.append( curr_node.value )

        elif curr_node.value >= partition_value:
          if linked_list_gt is None:
            linked_list_gt =LinkedList( curr_node.value )
          else:
            linked_list_gt.append( curr_node.value )

        # advance to next node
        curr_node =curr_node.next

      # join lists
      partitioned_linked_list =linked_list_lt
      if partitioned_linked_list is None:
        # then just return linked_list_gt
        partitioned_linked_list =linked_list_gt

      else: # then append linked_list_gt to linked_list_lt
        partitioned_linked_list.append_linked_list( linked_list_gt )

      self.head =partitioned_linked_list.head
      return partitioned_linked_list





#   +===================================================+
#   |               WRITE YOUR CODE HERE                |
#   | Description:                                      |
#   | - This method partitions a linked list around a   |
#   |   value `x`.                                      |
#   | - It rearranges the nodes so that all nodes less  |
#   |   than `x` come before all nodes greater or equal |
#   |   to `x`.                                         |
#   |                                                   |
#   | Tips:                                             |
#   | - We use two dummy nodes, `dummy1` and `dummy2`,  |
#   |   to build two separate lists: one for elements   |
#   |   smaller than `x` and one for elements greater   |
#   |   or equal to `x`.                                |
#   | - `prev1` and `prev2` help us keep track of the   |
#   |   last nodes in these lists.                      |
#   | - Finally, we merge these two lists by setting    |
#   |   `prev1.next = dummy2.next`.                     |
#   | - The head of the resulting list becomes          |
#   |   `dummy1.next`.                                  |
#   +===================================================+







# Function to convert linked list to Python list
def linkedlist_to_list(head):
  result = []
  current = head
  while current:
    result.append(current.value)
    current = current.next
  return result

# Function to test partition_list
def test_partition_list():
  test_cases_passed = 0

  print("-----------------------")

  # Test 1: Normal Case
  print("Test 1: Normal Case")
  x = 3
  print(f"x = {x}")
  ll = LinkedList(3)
  ll.append(1)
  ll.append(4)
  ll.append(2)
  ll.append(5)
  print("Before:", linkedlist_to_list(ll.head))
  ll.partition_list(x)
  print("After:", linkedlist_to_list(ll.head))
  if linkedlist_to_list(ll.head) == [1, 2, 3, 4, 5]:
    print("PASS")
    test_cases_passed += 1
  else:
    print("FAIL")

  print("-----------------------")

  # Test 2: All Equal Values
  print("Test 2: All Equal Values")
  x = 3
  print(f"x = {x}")
  ll = LinkedList(3)
  ll.append(3)
  ll.append(3)
  print("Before:", linkedlist_to_list(ll.head))
  ll.partition_list(x)
  print("After:", linkedlist_to_list(ll.head))
  if linkedlist_to_list(ll.head) == [3, 3, 3]:
    print("PASS")
    test_cases_passed += 1
  else:
    print("FAIL")

  print("-----------------------")

  # Test 3: Single Element
  print("Test 3: Single Element")
  x = 3
  print(f"x = {x}")
  ll = LinkedList(1)
  print("Before:", linkedlist_to_list(ll.head))
  ll.partition_list(x)
  print("After:", linkedlist_to_list(ll.head))
  if linkedlist_to_list(ll.head) == [1]:
    print("PASS")
    test_cases_passed += 1
  else:
    print("FAIL")

  print("-----------------------")

  # Test 4: Already Sorted
  print("Test 4: Already Sorted")
  x = 2
  print(f"x = {x}")
  ll = LinkedList(1)
  ll.append(2)
  ll.append(3)
  print("Before:", linkedlist_to_list(ll.head))
  ll.partition_list(x)
  print("After:", linkedlist_to_list(ll.head))
  if linkedlist_to_list(ll.head) == [1, 2, 3]:
    print("PASS")
    test_cases_passed += 1
  else:
    print("FAIL")

  print("-----------------------")

  # Test 5: Reverse Sorted
  print("Test 5: Reverse Sorted")
  x = 2
  print(f"x = {x}")
  ll = LinkedList(3)
  ll.append(2)
  ll.append(1)
  print("Before:", linkedlist_to_list(ll.head))
  ll.partition_list(x)
  print("After:", linkedlist_to_list(ll.head))
  if linkedlist_to_list(ll.head) == [1, 3, 2]:
    print("PASS")
    test_cases_passed += 1
  else:
    print("FAIL")

  print("-----------------------")

  # Test 6: All Smaller Values
  print("Test 6: All Smaller Values")
  x = 2
  print(f"x = {x}")
  ll = LinkedList(1)
  ll.append(1)
  ll.append(1)
  print("Before:", linkedlist_to_list(ll.head))
  ll.partition_list(x)
  print("After:", linkedlist_to_list(ll.head))
  if linkedlist_to_list(ll.head) == [1, 1, 1]:
    print("PASS")
    test_cases_passed += 1
  else:
    print("FAIL")

  print("-----------------------")

  # Test 7: Single Element, Equal to Partition
  print("Test 7: Single Element, Equal to Partition")
  x = 3
  print(f"x = {x}")
  ll = LinkedList(3)
  print("Before:", linkedlist_to_list(ll.head))
  ll.partition_list(x)
  print("After:", linkedlist_to_list(ll.head))
  if linkedlist_to_list(ll.head) == [3]:
    print("PASS")
    test_cases_passed += 1
  else:
    print("FAIL")

  print("-----------------------")

  # Summary
  print(f"{test_cases_passed} out of 7 tests passed.")


# Run the test function
test_partition_list()

"""
Implement the partition_list member function for the LinkedList class, which partitions the list such that all nodes with values less than x come before nodes with values greater than or equal to x.

Note:  This linked list class does NOT have a tail which will make this method easier to implement.

The original relative order of the nodes should be preserved.



Details:

The function partition_list takes an integer x as a parameter and modifies the current linked list in place according to the specified criteria. If the linked list is empty (i.e., head is null), the function should return immediately without making any changes.



Example 1:

Input:

Linked List: 3 -> 8 -> 5 -> 10 -> 2 -> 1 x: 5

Process:

Values less than 5: 3, 2, 1

Values greater than or equal to 5: 8, 5, 10

Output:

Linked List: 3 -> 2 -> 1 -> 8 -> 5 -> 10





Example 2:
Input:

Linked List: 1 -> 4 -> 3 -> 2 -> 5 -> 2 x: 3

Process:

Values less than 3: 1, 2, 2

Values greater than or equal to 3: 4, 3, 5

Output:

Linked List: 1 -> 2 -> 2 -> 4 -> 3 -> 5





Tips:

While traversing the linked list, maintain two separate chains: one for values less than x and one for values greater than or equal to x.

Use dummy nodes to simplify the handling of the heads of these chains.

After processing the entire list, connect the two chains to get the desired arrangement.



Note:

The solution must maintain the relative order of nodes. For instance, in the first example, even though 8 appears before 5 in the original list, the partitioned list must still have 8 before 5 as their relative order remains unchanged.

Note:

You must solve the problem WITHOUT MODIFYING THE VALUES in the list's nodes (i.e., only the nodes' next pointers may be changed.)
"""