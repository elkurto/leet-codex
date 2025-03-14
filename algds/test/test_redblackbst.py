import unittest
from ..redblackbst import Rbtree

"""
  # to run this file
  cd leet-codex/
  python3 -m algds.test.test_redblackbst
"""
class TestRbtree(unittest.TestCase):

  def test_put_get_001(self):
    rbtree =Rbtree()
    rbtree.put(1,'A')
    node =rbtree.get(1)
    self.assertEqual( node.value, 'A')

  def test_put_get_002(self):
    rbtree =Rbtree()
    rbtree.put(1,'A')
    rbtree.put(3,'C')
    rbtree.put(4,'D')

    node =rbtree.get(1)
    self.assertEqual( node.value, 'A')

    node_003 =rbtree.get(3)
    self.assertEqual( node_003.value, 'C')

    node_004 =rbtree.get(4)
    self.assertEqual( node_004.value, 'D')

    node_005 =rbtree.get(5)
    self.assertIsNone(node_005)


if __name__ == "__main__":
  unittest.main()
