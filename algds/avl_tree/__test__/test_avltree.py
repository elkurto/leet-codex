import unittest
from avl_tree import AVLTree

class TestAvlTree(unittest.TestCase):


  def test_insert_and_print(self):
    a =AVLTree()
    a.insert( 37 , '37')
    a.insert( 19 , '19')
    a.insert( 49 , '49')

    a.print(2)
    #   AVL>49 ( 1 0 )
    # AVL>37 ( 2 0 )
    #   AVL>19 ( 1 0 )

    self.assertEqual(37, a.root.key)
    self.assertEqual( 19, a.root.left.key )
    self.assertEqual( 49, a.root.right.key )

if __name__ == "__main__":
  unittest.main()