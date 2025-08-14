# Implement AVL trees using Tree and Node classes
# These are balanced binary trees

class SimpleStack:
  def __init__(self):
    self.ary =[]

  def pop(self):
    return self.ary.pop()
  def push(self, elem):
    return self.ary.append(elem)
  def is_empty(self):
    return len(self.ary) <= 0

class NodeAvl(object):      # A node in an AVL tree
  def __init__(           # Constructor takes a key-data pair
          self,             # since every node must have 1 item
          key, data):
    self.key, self.data = key, data # Store item key & data
    self.left = self.right = None   # Empty child links
    self.height =0
    self.update_height()  # Set initial height of node


  def update_height(self): # Update height of node from children
    self.height = max(   # Get maximum child height using 0 for
      child.height if child else 0 # empty child links
      for child in (self.left, self.right)
    ) + 1                # Add 1 for this node

  def compute_height_diff(self):   # Return difference in child heights
    left  = self.left.height  if self.left  else 0
    right = self.right.height if self.right else 0
    return left - right  # Return difference in heights

  def __str__(self):      # Represent a node as a string using a
    return 'AVL>' + str(self.key) # prefix and its key

class AVLTree(object):

  def __init__(self):        # Constructor for empty AVL tree
    self.root = None      # No root node in empty tree

  def is_empty(self):         # Check for empty tree
    return self.root is None

  @classmethod
  def __find(cls, goal, node): # Find a node that matches goal key
    while node is not None: # Loop until we reach an empty link
      if node.key == goal: # Check if current node's key matches
        return node       # and return it if it does
      elif goal < node.key: # Else if goal is below current node,
        node = node.left  # then search left subtree
      else:
        node = node.right # Else search the right subtree
    return None             # If loop ends, goal wasn't found

  def search(self, goal):    # Search for an item whose key matches a
    node = self.__find(goal, self.root) # goal starting at root
    # Return the node's data, if found
    return node.data if node else None

  def insert(self, key, data): # Insert an item into the AVL tree
    self.root, flag = self._insert( # Reset the root to be the
      self.root, key, data) # modified tree and return the
    return flag             # the insert vs. update flag

  def _insert(self,  # Insert an item into an AVL subtree
              node,  # rooted a particular node, returning
              key, data):   # the modified node & insertion flag
    if node is None:        # For an empty subtree, return a new
      return NodeAvl(key, data), True # node in the tree

    if key == node.key:     # If node already has the insert key,
      node.data = data     # then update it with the new data
      return node, False   # Return the node and False for flag

    elif key < node.key:    # Does the key belong in left subtree?
      node.left, flag = self._insert( # If so, insert on left and
        node.left, key, data) # update the left link
      if node.compute_height_diff() > 1: # If insert made node left heavy

        if node.left.key < key: # If inside grandchild inserted,
          # then raise grandchild
          node.left = self.rotate_left( node.left)

        # Correct left heavy tree by
        # rotating right around this node
        node = self.rotate_right( node)

    else:                   # Otherwise key belongs in right subtree
      node.right, flag = self._insert( # Insert it on right and
        node.right, key, data) # update the right link
      if node.compute_height_diff() < -1: # If insert made node right heavy

        if key < node.right.key: # If inside grandchild inserted,
          node.right = self.rotate_right( # then raise grandchild
            node.right)

        node = self.rotate_left( # Correct right heavy tree by
          node)          # rotating left around this node

    node.update_height()     # Update this node's height
    return node, flag       # Return the updated node & insert flag

  @classmethod
  def rotate_right(cls, top): # Rotate a subtree to the right
    """
                                                      +-p
                                                     o
          +-p    rotate_right( top=m )              / +-n
         o        - to_raise =b (top.left)         m
        / +-n     - m.left =c (to_raise.right)    / +-c
       m          - b.right =m (top)             b
        \ +-c     - update_heights                +-a
         b        - return b (to_raise) so that
          +-a        parent can update ref_to_child.
    """
    to_raise = top.left       # to_raise =k  # The node to raise is top's left child
    top.left = to_raise.right # m.left =c    # The raised node's right crosses over
    to_raise.right = top      # k.right =m   # to be the left subtree under the old
    top.update_height()       #              # top.  Then the heights must be updated
    to_raise.update_height()
    return to_raise          # Return raised node to update parent

  @classmethod
  def rotate_left(cls, top): # Rotate a subtree to the left
    """
          +-p   rotate_left( top=m )                   +-p
        o        - to_raise =o (top.right)           o
       /  +-n*   - m.right  =n*(to_raise.left)        \  +-n*
      m          - o.left   =m (top)                   m
       \  +-c    - update_heights                       \  +-c
        b        - return o (to_raise) so that           b
          +-a        parent can update ref_to_child.       +-a

    """
    to_raise = top.right     # The node to raise is top's right child
    top.right = to_raise.left # The raised node's left crosses over
    to_raise.left = top      # to be the right subtree under the old
    top.update_height()      # top.  Then the heights must be updated
    to_raise.update_height()
    return to_raise          # Return raised node to update parent

  def traverse(self,  # Non-recursive generator to traverse
               traverse_type='in'): # tree in pre, in, or post order
    if traverse_type not in [ # Verify traversal type is an
      'pre', 'in', 'post']: # accepted value
      raise ValueError(
        "Unknown traversal type: " + str(traverse_type))

    stack =SimpleStack()         # Create a stack
    stack.push(self.root) # Put root node in stack

    while not stack.is_empty(): # While there is work in the stack
      item = stack.pop() # Get next item
      if isinstance(item, NodeAvl): # If it's a tree node
        if traverse_type == 'post': # For post-order, put it last
          stack.push((item.key, item.data))
        stack.push(item.right) # Traverse right child
        if traverse_type == 'in': # For pre-order, put item 2nd
          stack.push((item.key, item.data))
        stack.push(item.left)  # Traverse left child
        if traverse_type == 'pre': # For pre-order, put item 1st
          stack.push((item.key, item.data))
      elif item:           # Every other non-None item is a
        yield item        # (key, value) pair to be yielded

  def print(self,  # Print a tree sideways with 1 node
            indent_by=4):     # on each line and indenting each level
    self._print_subtree(self.root,  # by some blanks.  Start at root node
                 "", indent_by) # with no indent

  def _print_subtree(self,  # Recursively print a subtree, sideways
                     node,  # with the root node left justified
                     indent,  # using indent as prefix for its level
                     indent_by=4):   # Increase indent level for subtrees
    if node:                # Only print if there is a node
      self._print_subtree(node.right,  # Print the right subtree
                          indent + " " * indent_by, indent_by)
      print(indent, node, '(',  # Print this node, its height, &
            node.height, node.compute_height_diff(), ')') # balance
      self._print_subtree(node.left,  # Print the left subtree
                          indent + " " * indent_by, indent_by)

  def __str__(self):         # Show tree in string form as key-value
    return '{{{}}}'.format( # pairs surrounded in curly braces
      ', '.join('{}: {}'.format( # Pairs are formatted key: value
        repr(key), repr(val))
                for key, val in self.traverse('pre')))

  def delete(self, goal):    # Delete a node whose key matches goal

    # Delete starting at root and  update root link
    self.root, flag = self._delete(  self.root, goal)
       
    return flag             # Return flag indicating goal node found

  def _delete(self,  node, goal):
    # Delete matching goal key from subtree  rooted at node.
    # Return modified node
    if node is None:        # If subtree is empty,
      return None, False   # then no matching goal key

    if goal < node.key:
      # then continue search for goal in left-subtree.

      # If goal exists, then delete goal, update the left link and store flag
      node.left, flag = self._delete( node.left, goal)

      node = self._balance_left(node) # Correct any imbalance

    elif goal > node.key:
      # then continue search for goal in left-subtree.

      # If goal exists, then delete goal, update the right link and store flag
      node.right, flag = self._delete(node.right, goal)

      node = self._balance_right(node) # Correct any imbalance

    # Else node's key matches goal, so determine deletion case
    elif node.left is None: # If no left child, return right child
      return node.right, True # as remainder, flagging deletion
    elif node.right is None: # If no right child, return left child
      return node.left, True # as remainder, flagging deletion
    # Deleted node has two children so find successor in right
    else:                   # subtree and replace this item
      node.key, node.data, node.right= self._delete_min(node.right)
      node = self._balance_right(node) # Correct any imbalance
      flag = True          # The goal was found and deleted

    node.update_height()     # Update height of node after deletion
    return node, flag       # Return modified node and delete flag

  def _delete_min(           # Find minimum node of subtree, delete
          self,                # it, return minimum key, data pair and
          node):               # updated link to parent
    if node.left is None:   # If left child link is empty
      # , then node contains min_key
      #   and node.right replaces node.
      return node.key, node.data, node.right

    # Else, continue search for min_key in left subtree
    key, data, node.left = self._delete_min( node.left)

    node = self._balance_left(node) # Correct any imbalance
    node.update_height()     # Update height of node
    return key, data, node

  def _balance_left(self, node): # Rebalance after left deletion
    if node.compute_height_diff() < -1: # If node is right heavy, then
      if node.right.compute_height_diff() > 0: # If the right child is left
        node.right = self.rotate_right( # heavy, then rotate
          node.right)    # it to the right first

      node = self.rotate_left( # Correct right heavy tree by
        node)             # rotating left around this node
    return node             # Return top node

  def _balance_right(self, node): # Rebalance after right deletion
    if node.compute_height_diff() > 1: # If node is left heavy, then
      if node.left.compute_height_diff() < 0: # If the left child is right
        node.left = self.rotate_left( # heavy, then rotate
          node.left)     # it to the left first

      node = self.rotate_right( # Correct left heavy tree by
        node)             # rotating right around this node
    return node             # Return top node