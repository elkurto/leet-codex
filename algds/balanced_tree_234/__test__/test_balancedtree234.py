import unittest
from balanced_tree_234 import Node234,BalancedTree234

class TestBalancedTree234(unittest.TestCase):
  def test_ctor(self):
    b =BalancedTree234()
    self.assertIsNone( b.root )
    self.assertEqual( 0, b.population)
    self.assertTrue( b.is_empty())

  def test_insert_01_node(self):
    b =BalancedTree234()
    b.insert(100, '100-data')

    self.assertEqual( [100,None,None], b.root.keys[0:3])
    self.assertEqual( 1, b.population)
    # @todo test state of data and childen

  def test_insert_02_key(self):
    b =BalancedTree234()
    b.insert(100, '100-data')
    b.insert( 50, '050-data')

    self.assertEqual( [50,100,None], b.root.keys[0:3])
    self.assertEqual( 2, b.population)

  def test_insert_03_key(self):
    b =BalancedTree234()
    b.insert(100, '100-data')
    b.insert( 50, '050-data')
    b.insert( 25, '025-data')

    self.assertEqual( [25, 50, 100], b.root.keys[0:3])
    self.assertEqual( 3, b.population)

  def test_split_root(self):
    b =BalancedTree234()
    b.insert(100, '100-data')
    b.insert( 50, '050-data')
    b.insert( 25, '025-data')

    self.assertEqual( [25, 50, 100], b.root.keys[0:3])
    self.assertEqual( 3, b.population)
    self.assertTrue( b.root.is_leaf() )

    b.insert(150, '150-data')
    self.assertEqual( [50,None,None], b.root.keys[0:3])
    self.assertFalse( b.root.is_leaf() )

    child00 =b.root.children[0]
    self.assertEqual( [25,None,None], child00.keys[0:3])

    child01 =b.root.children[1]
    self.assertEqual( [100,150,None], child01.keys[0:3])




if __name__ == '__main__':
  unittest.main()
