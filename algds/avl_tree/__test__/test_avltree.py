import unittest
from avl_tree import AVLTree

class TestAvlTree(unittest.TestCase):

  def test_is_empty(self):
    a =AVLTree()
    self.assertTrue( a.is_empty() )

  def test_insert_and_print(self):
    a =AVLTree()
    a.insert( 37 , '37')
    a.insert( 19 , '19')
    a.insert( 49 , '49')

    a.print(2)
    #   AVL>49 ( 1 0 )
    # AVL>37 ( 2 0 )
    #   AVL>19 ( 1 0 )

    self.assertEqual( 49, a.root.right.key )
    self.assertEqual(37, a.root.key)
    self.assertEqual( 19, a.root.left.key )


  def test_insert_49_37_19(self):
    a =AVLTree()
    a.insert( 49 , '49')
    a.insert( 37 , '37')
    a.insert( 19 , '19')


    a.print(2)
    #   AVL>49 ( 1 0 )
    # AVL>37 ( 2 0 )
    #   AVL>19 ( 1 0 )

    self.assertEqual( 49, a.root.right.key )
    self.assertEqual(37, a.root.key)
    self.assertEqual( 19, a.root.left.key )


  def test_insert_searchexamploz(self):
    a =AVLTree()
    for char in "searchxmploz":
      print( f"\n\ninserting {char}-------")
      a.insert(char, char*3)
      a.print(2)

    self.assertEqual( 'zzz', a.search('z'))
    self.assertEqual( 'm', a.root.key)

  def test_delete(self):
    a =AVLTree()
    for char in "searchxmploz":
      a.insert(char, char*3)
    #end-for

    a.print(2)
    #        AVL>z ( 1 0 )
    #      AVL>x ( 2 0 )
    #        AVL>s ( 1 0 )
    #    AVL>r ( 3 0 )
    #      AVL>p ( 2 1 )
    #        AVL>o ( 1 0 )
    #  AVL>m ( 4 0 )
    #        AVL>l ( 1 0 )
    #      AVL>h ( 2 -1 )
    #    AVL>e ( 3 0 )
    #        AVL>c ( 1 0 )
    #      AVL>a ( 2 -1 )

    self.assertEqual( 'zzz', a.search('z'))
    self.assertTrue( a.delete('z'))
    self.assertIsNone(  a.search('z'))

    # delete interior node, r
    self.assertEqual( 'r' , a.root.right.key )
    b_did_delete =a.delete('r')
    self.assertTrue( b_did_delete)
    # node:s replaces node:r because s is the successor of r.
    self.assertEqual( 's' , a.root.right.key )



    a.print(2)
    #      AVL>x ( 1 0 )
    #    AVL>s ( 3 1 )
    #      AVL>p ( 2 1 )
    #        AVL>o ( 1 0 )
    #  AVL>m ( 4 0 )
    #        AVL>l ( 1 0 )
    #      AVL>h ( 2 -1 )
    #    AVL>e ( 3 0 )
    #        AVL>c ( 1 0 )
    #      AVL>a ( 2 -1 )

if __name__ == "__main__":
  unittest.main()