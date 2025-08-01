import unittest
from balanced_tree_234 import Node234,BalancedTree234

class TestBalancedTree234(unittest.TestCase):
  def test_ctor(self):
    b =BalancedTree234()
    self.assertIsNone( b.root )
    self.assertEqual( 0, b.population)
    self.assertTrue( b.is_empty())

  
if __name__ == '__main__':
  unittest.main()
