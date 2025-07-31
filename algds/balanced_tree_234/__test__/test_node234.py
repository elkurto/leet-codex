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
    node =Node234('m', 'mmmm', Node234('b', 'bbbb'), Node234('r', 'rrrr'))
    node.insert_key_value( 'k', 'kkkk')
    self.assertListEqual( ['k','m',None], node.keys[0:3])

    node.insert_key_value( 'r', 'rrrr')
    self.assertListEqual( ['k','m','r'], node.keys[0:3])

    self.assertRaises( Exception, node.insert_key_value, 'd', 'dddd')



  def test_is_full_and_is_not_full(self):
    node =Node234( 'm', 'mmmm')
    self.assertFalse( node.is_full() )
    self.assertTrue( node.is_not_full() )

    node.insert_key_value('k', 'kkkk')
    self.assertFalse( node.is_full() )
    self.assertTrue( node.is_not_full() )

    node.insert_key_value('i', 'iiii')
    self.assertTrue( node.is_full() )
    self.assertFalse( node.is_not_full() )

    self.assertListEqual(['i','k','m'], node.keys[0:3])

  def test_pop_key_data(self):
    node =Node234( 'm', 'mmmm')
    node.insert_key_value('k', 'kkkk')
    node.insert_key_value('i', 'iiii')

    key,data =node.pop_key_data(idx=1)
    self.assertEqual( 'k', key)
    self.assertEqual( 'kkkk', data)

    self.assertListEqual(['i','m',None], node.keys[0:3])

  def test_split_full_node(self):
    node_left =Node234( 'o', 'oooo', )
    node_left.insert_key_value('m', 'mmmm')
    node_left.insert_key_value('r', 'rrrr')

    node_right =node_left.split_full_node()
    self.assertEqual( 'r', node_right.keys[0])

  def receive_middle_from_child(self, key, data):
    # todo
    pass



if __name__ == '__main__':
  unittest.main()
