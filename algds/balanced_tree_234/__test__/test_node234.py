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

  def test_insert_key_value(self):
    # todo

  def test_is_full_and_is_not_full(self):
    # todo

  def test_pop_key_data(self):
    # todo

  def test_split_full_node(self):
    # todo

  def receive_middle_from_child(self, key, data):
    # todo




if __name__ == '__main__':
  unittest.main()
