import unittest
from balanced_tree_234 import StackFixedSize

class TestStackFixedSize(unittest.TestCase):
  def test_foo(self):
    self.assertTrue(True)

  def test_append(self):
    s =StackFixedSize( 5)
    s.append( 0 )
    s.append( 1 )
    self.assertEqual( len(s), 2)

    s.append( 2)
    s.append( 3)
    s.append( 4)
    self.assertRaises(IndexError, s.append, 5)


  def test_index(self):
      s =StackFixedSize( 5)
      s.append(3)
      s.append(4)
      self.assertEqual( s[0] , 3)
      self.assertEqual( s[1] , 4)

  def test_set_index(self):
    s =StackFixedSize( 5)
    s.push( 0 )
    s.push( 1 )
    s.push( 2 )

    self.assertEqual( s[0], 0)
    self.assertEqual( s[1], 1)
    self.assertEqual( s[2], 2)

    self.assertRaises(IndexError, s.set_element_at_index, 4, 1000)
    self.assertRaises(IndexError, s.set_element_at_index, 5, 1000)

    rval =s.set_element_at_index(2,222)
    self.assertEqual( 2, rval)

  def test_pop(self):
    s =StackFixedSize( 5)
    s.push( 0 )
    s.push( 1 )
    s.push( 2 )

    self.assertEqual( s.pop(), 2)
    self.assertEqual( s.pop(), 1)
    self.assertEqual( s.pop(), 0)

  def test_pop_idx(self):
    s =StackFixedSize(5)
    s.push( 0 )
    s.push( 1 )
    s.push( 2 )
    s.push( 3 )
    s.push( 4 )
    self.assertEqual( 5, len(s))
    self.assertEqual( 1, s.pop(1))
    self.assertListEqual( [0,2,3,4,None], s[0:5])

    self.assertEqual( 4, len(s))
    self.assertEqual( 2, s.pop(1))
    self.assertListEqual( [0,3,4,None,None], s[0:5])

    self.assertEqual( 3, len(s))
    self.assertEqual( 3, s.pop(1))
    self.assertListEqual( [0,4,None,None,None], s[0:5])

    self.assertEqual( 2, len(s))
    self.assertEqual( 4, s.pop(1))
    self.assertListEqual( [0,None,None,None,None], s[0:5])

    self.assertEqual( 1, len(s))
    self.assertEqual( 0, s.pop(0))
    self.assertListEqual( [None,None,None,None,None], s[0:5])
    self.assertEqual( 0, len(s))





  def test_insert_at(self):
    s =StackFixedSize( 4)

    s.insert_at(1, 'a')
    self.assertEqual('a', s[0])
    self.assertEqual( 1, len(s))

    s.insert_at(3, 'c')
    self.assertEqual('a', s[0])
    self.assertEqual('c', s[1])
    self.assertEqual( 2, len(s))

    s.insert_at(1, 'b')
    self.assertEqual('a', s[0])
    self.assertEqual('b', s[1])
    self.assertEqual('c', s[2])
    self.assertEqual( 3, len(s))


    s.insert_at( 0, 'z')
    self.assertEqual('z', s[0])
    self.assertEqual('a', s[1])
    self.assertEqual('b', s[2])
    self.assertEqual('c', s[3])
    self.assertEqual( 4, len(s))

    s.insert_at( 1, 'x')
    self.assertEqual('z', s[0])
    self.assertEqual('x', s[1])
    self.assertEqual('a', s[2])
    self.assertEqual('b', s[3])
    self.assertEqual( 4, len(s))

    s.insert_at( 1, 'y')
    self.assertEqual('z', s[0])
    self.assertEqual('y', s[1])
    self.assertEqual('x', s[2])
    self.assertEqual('a', s[3])
    self.assertEqual( 4, len(s))


if __name__ == "__main__":
  unittest.main()