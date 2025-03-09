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
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.length = 0

    def advance_ptr_by_n( self, ptr, n):
        for i in range(0,n):
            ptr =ptr.next
        return ptr

    def swap_node_values( self, nodea, nodeb):
        temp =nodea.value
        nodea.value =nodeb.value
        nodeb.value =temp

    def reverse_between(self, s, e):
        if self.head is None:
            return None
        if not (0 <= s < self.length):
            raise IndexError( 's must be in [0,{0}]'.format( self.length-1 ))
        if not (0 <= e < self.length):
            raise IndexError( 'e must be in [0,{0}]'.format( self.length-1 ))
    
        left =self.advance_ptr_by_n( self.head, s)
        right =self.advance_ptr_by_n( left, e-s)
        
        while s < e:
            self.swap_node_values( left, right)
            s +=1
            e -=1
            left =left.next
            right =self.advance_ptr_by_n( left, e-s)




linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

# Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty()
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Original linked list: 
    1
    2
    3
    4
    5
    Reversed sublist (2, 4): 
    1
    2
    5
    4
    3
    Reversed entire linked list: 
    3
    4
    5
    2
    1
    Reversed sublist of length 1 (3, 3): 
    3
    4
    5
    2
    1
    Reversed empty linked list: 
    None
    
"""