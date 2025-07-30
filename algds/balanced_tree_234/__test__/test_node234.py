import unittest
from balanced_tree_234 import Node234

class MyTestCase(unittest.TestCase):
  def test_ctor(self):
    node =Node234()
    self.assertEqual(0, node.nkey())
    self.assertEqual(0, node.ndata())
    self.assertEqual(0, node.nchild())

  def test_ctor_with_param(self):
    node =Node234('b', 'bbbb', Node234('a', 'aaaa'), Node234('c', 'cccc'))
    self.assertEqual(1, node.nkey())
    self.assertEqual(1, node.ndata())
    self.assertEqual(2, node.nchild())
    self.assertTrue( node.is_valid_or_raise() )




if __name__ == '__main__':
  unittest.main()
