import unittest
from ..redblackbst import Rbtree

"""
  cd leet-codex/
  python3 -m algds.test.test_redblackbst
"""

class TestRbtree(unittest.TestCase):

  def test_root_none_initially(self):
    rbtree =Rbtree()
    self.assertIsNone( rbtree.root )


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

  def test_put_m_r(self):
    rbtree =Rbtree()

    # after put m
    rbtree.put( 'm', 'm');
    self.assertEqual( 'm', rbtree.root.value  )

    # after put m and put r
    rbtree.put( 'r', 'r');
    self.assertEqual( 'r', rbtree.root.value )
    self.assertIsNone( rbtree.root.right )
    self.assertEqual( 'm', rbtree.root.left.value )

  def test_put_m_p_r(self):
    rbtree =Rbtree()
    # after put m
    rbtree.put( 'm', 'm')
    self.assertEqual( 'm', rbtree.root.value  )

    # after put m and put r
    rbtree.put( 'r', 'r')
    self.assertEqual( 'r', rbtree.root.value )
    self.assertIsNone( rbtree.root.right )
    self.assertEqual( 'm', rbtree.root.left.value )

    rbtree.put('p','p')
    self.assertEqual( 'p',  rbtree.root.value )
    self.assertEqual( 'm' , rbtree.root.left.value )
    self.assertEqual( 'r',  rbtree.root.right.value )


  """
                      m
           e----------+-----------r
       ----+----             -----+----
       c       l             p        x
     ==+--   ==+--                  ==+--
     a       h                      s
  """
  def test_put_s_e_a_r_c_h_x_m_p_l(self):
    rbtree =Rbtree()
    keystring ='searchxmpl'
    for key in keystring:
      rbtree.put( key, key)


    # root
    self.assertEqual( 'm',  rbtree.root.value )

    # right sub tree of root
    self.assertEqual('r', rbtree.root.right.value)
    self.assertEqual( 'p', rbtree.root.right.left.value)
    self.assertEqual( 'x', rbtree.root.right.right.value )
    self.assertEqual( 's', rbtree.root.right.right.left.value )

    # left sub tree of root
    self.assertEqual('e', rbtree.root.left.value )

    # left subtree of e
    self.assertEqual('c', rbtree.root.left.left.value  )
    self.assertEqual('a', rbtree.root.left.left.left.value)
    self.assertIsNone( rbtree.root.left.left.right )

    # right subtree of e
    self.assertEqual('l', rbtree.root.left.right.value)
    self.assertEqual('h', rbtree.root.left.right.left.value)
    self.assertIsNone(rbtree.root.left.right.right )

  def test_contains_searchxmpl(self):
    rbtree =Rbtree()
    keystring ='searchxmpl'
    for key in keystring:
      rbtree.put( key, key)

    self.assertTrue( rbtree.contains( 'm' ))
    self.assertFalse( rbtree.contains( 'z' ))
    self.assertTrue( rbtree.contains( 'h' ))
    self.assertTrue( rbtree.contains( 's' ))
    self.assertFalse( rbtree.contains( None ))
    self.assertTrue( rbtree.contains( 'r' ))
    self.assertTrue( rbtree.contains( 'x' ))

  def test_delete_r_from_searchxmpl(self):
    rbtree =Rbtree()
    keystring = 'searchxmpl'
    for key in keystring:
      rbtree.put(key, key)

    rbtree.delete( 'r' )
    self.assertFalse( rbtree.contains( 'r' ))

  def test_delete_m_from_searchxmpl(self):
    rbtree =Rbtree()
    keystring = 'searchxmpl'
    for key in keystring:
      rbtree.put(key, key)

    rbtree.delete( 'm' )
    self.assertFalse( rbtree.contains( 'm' ))
    self.assertEqual( 'p', rbtree.root.value )

  def test_delete_l_from_searchxmpl(self):
    rbtree =Rbtree()
    keystring = 'searchxmpl'
    for key in keystring:
      rbtree.put(key, key)

    rbtree.delete( 'l' )
    self.assertFalse( rbtree.contains( 'l' ))

  def test_to_list_in_order(self):

    rbtree =Rbtree()
    keystring ='searchxmpl'
    for key in keystring:
      rbtree.put( key, key)

    list_value =rbtree.to_list()
    self.assertEqual( len(keystring), len(list_value) )
    self.assertEqual( 'a,c,e,h,l,m,p,r,s,x', ','.join(list_value))


if __name__ == "__main__":
  unittest.main()
