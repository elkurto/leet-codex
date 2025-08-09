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

  def test_insert_sear(self):
    chars ="sear"
    b =BalancedTree234()
    # insert each character as a key
    for char in chars:
      b.insert(char, char*3)

    # validate
    self.assertListEqual(['e',None,None], b.root.keys[0:3])
    self.assertEqual( 2, b.root.nchild())
    c0 =b.root.children[0]
    c1 =b.root.children[1]
    self.assertIsInstance(c0, Node234)
    self.assertIsInstance(c1, Node234)

    self.assertListEqual( ['a',None,None], c0.keys[0:3])
    self.assertListEqual( ['r','s',None],  c1.keys[0:3])

  def test_insert_seart(self):
    chars ="seart"
    b =BalancedTree234()
    # insert each character as a key
    for char in chars:
      b.insert(char, char*3)

    # validate
    self.assertListEqual(['e',None,None], b.root.keys[0:3])
    self.assertEqual( 2, b.root.nchild())
    c0 =b.root.children[0]
    c1 =b.root.children[1]
    self.assertIsInstance(c0, Node234)
    self.assertIsInstance(c1, Node234)

    self.assertListEqual( ['a',None,None], c0.keys[0:3])
    self.assertListEqual( ['r','s','t'],  c1.keys[0:3])

  def test_insert_seartu(self):
    chars ="seart"
    b =BalancedTree234()
    # insert each character as a key
    for char in chars:
      b.insert(char, char*3)

    b.insert('u', 'u'*3)
    # validate
    self.assertListEqual(['e','s',None], b.root.keys[0:3])
    self.assertEqual( 3, b.root.nchild())
    c0 =b.root.children[0]
    c1 =b.root.children[1]
    c2 =b.root.children[2]

    self.assertIsInstance(c0, Node234)
    self.assertIsInstance(c1, Node234)
    self.assertIsInstance(c2, Node234)

    self.assertListEqual( ['a',None,None], c0.keys[0:3])
    self.assertListEqual( ['r',None,None],  c1.keys[0:3])
    self.assertListEqual( ['t','u',None],  c2.keys[0:3])

  def test_insert_searchxmpl(self):
    chars ="searchxmpl"
    b =BalancedTree234()
    # insert each character as a key
    for char in chars:
      b.insert(char, char*3)

    # validate
    self.assertListEqual(['e','m','r'], b.root.keys[0:3])
    self.assertEqual( 4, b.root.nchild())
    c0 =b.root.children[0]
    c1 =b.root.children[1]
    c2 =b.root.children[2]
    c3 =b.root.children[3]
    self.assertIsInstance(c0, Node234)
    self.assertIsInstance(c1, Node234)
    self.assertIsInstance(c2, Node234)
    self.assertIsInstance(c3, Node234)

    self.assertListEqual( ['a','c',None], c0.keys[0:3])
    self.assertListEqual( ['h','l',None], c1.keys[0:3])
    self.assertListEqual( ['p',None,None], c2.keys[0:3])
    self.assertListEqual( ['s','x',None], c3.keys[0:3])

  def test_traverse_pre_order(self):
    chars ="searchxmpl"
    b =BalancedTree234()
    # insert each character as a key
    for char in chars:
      b.insert(char, char*3)

    ary_keys =[]
    def fn_visit_accumulate( x ):
      ary_keys.append(x)

    b.traverse_pre_order(fn_visit_accumulate)
    ary_expected =['a','c','e','h','l','m','p','r','s','x']
    self.assertListEqual(ary_expected, ary_keys)

  def test_traverse_in_order(self):
    chars ="searchxmpl"
    b =BalancedTree234()
    # insert each character as a key
    for char in chars:
      b.insert(char, char*3)

    ary_string_representation =[]
    def fn_visit_accumulate( node, curr_stack, chlld_stack ):
      ary_string_representation.append( str(node.keys) )

    b.traverse_in_order(fn_visit_accumulate)
    ary_expected =['e,m,r','a,c,None','h,l,None','p,None,None', 's,x,None']
    self.assertListEqual(ary_expected, ary_string_representation)


  def test_do_fusion_left(self):
    chars ="searchxmplbz"
    b =BalancedTree234()
    # insert each character as a key
    for char in chars:
      b.insert(char, char*3)

    b.print_tree()
    # m,None,None|
    # e,None,None  r,None,None|
    # a,b,c  h,l,None  p,None,None  s,x,z|

    b.insert('o', 'ooo')
    # m,None,None|
    # e,None,None  r,None,None|
    # a,b,c  h,l,None  o,p,None  s,x,z|
    b.print_tree()
    self.assertListEqual( ['m',None,None], b.root.keys[0:3])

    # make a fusion occur at root by deleting z
    key,data =b._delete_max_in_subtree(b.root, None)
    b.print_tree()
    # e,m,r|
    # a,b,c  h,l,None  o,p,None  s,x,None|
    self.assertListEqual( ['e','m','r'], b.root.keys[0:3])
    self.assertEqual( 'z', key)
    self.assertEqual( 'zzz', data)

    # make a split occur at root by re-inserting z
    b.insert( 'z', 'zzz')
    self.assertListEqual( ['m',None,None], b.root.keys[0:3])
    b.print_tree()
    # m,None,None|
    # e,None,None  r,None,None|
    # a,b,c  h,l,None  o,p,None  s,x,z|
    self.assertEqual( 's,x,z', b.root.children[1].children[1].to_csv_keys())


  def test_delete_min_in_subtree(self):
    chars ="searchxmpl"
    b =BalancedTree234()
    # insert each character as a key
    for char in chars:
      b.insert(char, char*3)

    b.print_tree()
    # e,m,r|
    # a,c,None  h,l,None  p,None,None  s,x,None|
    key,data =b._delete_min_in_subtree( b.root, None )
    self.assertEqual('a', key)
    self.assertEqual('aaa', data)

    b.print_tree()
    # e,m,r|
    # c,None,None  h,l,None  p,None,None  s,x,None|
    key,data =b._delete_min_in_subtree( b.root, None )
    self.assertEqual('c', key)
    self.assertEqual('ccc', data)

    b.print_tree()
    # h,m,r|
    # e,None,None  l,None,None  p,None,None  s,x,None|

    key,data =b._delete_min_in_subtree( b.root, None )
    self.assertEqual('e', key)
    self.assertEqual('eee', data)

    b.print_tree()
    # h,m,r|
    # e,None,None  l,None,None  p,None,None  s,x,None|

  def test_delete_max_in_subtree(self):
    chars ="searchxmpl"
    b =BalancedTree234()
    # insert each character as a key
    for char in chars:
      b.insert(char, char*3)

    b.print_tree()
    # e,m,r|
    # a,c,None  h,l,None  p,None,None  s,x,None|

    key,data =b._delete_max_in_subtree( b.root, None )
    self.assertEqual('x', key)
    self.assertEqual('xxx', data)

    b.print_tree()
    # e,m,r|
    # a,c,None  h,l,None  p,None,None  s,None,None|

    key,data =b._delete_max_in_subtree( b.root, None )
    self.assertEqual('s', key)
    self.assertEqual('sss', data)

    b.print_tree()
    # e,m,None|
    # a,c,None  h,l,None  p,r,None|

  def test_remove(self):
    pass


if __name__ == '__main__':
  unittest.main()

# todo - test do_fusion_left at when curr ==self.root
# todo - test remove( target )