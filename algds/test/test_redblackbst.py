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

"""
@todo convert these tests to python
describe('test Rbtree 001', () => {

  it( 'init Rbtree', () => {
    let rbtree =new Rbtree();
    expect( rbtree.root ).toBeNull();
  })

  it( 'Rbtree::put - m', () =>{
    let rbtree =new Rbtree();
    rbtree.put( 'm', 'm');
    expect( rbtree.root.val ).toBe('m');
  })

  it( 'Rbtree::put - m,r', () =>{
    let rbtree =new Rbtree();
    rbtree.put( 'm', 'm');
    expect( rbtree.root.val ).toBe('m');
    rbtree.put( 'r', 'r');
    expect( rbtree.root.val ).toBe('r');
    expect( rbtree.root.right ).toBeNull();
    expect( rbtree.root.left.val ).toBe('m');
  })

  it( 'Rbtree::put - m,r,p', () =>{
    let rbtree =new Rbtree();
    rbtree.put( 'm', 'm');
    expect( rbtree.root.val ).toBe('m');

    rbtree.put( 'r', 'r');
    expect( rbtree.root.val ).toBe('r');
    expect( rbtree.root.right ).toBeNull();
    expect( rbtree.root.left.val ).toBe('m');
    expect( rbtree.root.left.color ).toBe( true );

    rbtree.put('p','p');
    expect( rbtree.root.val ).toBe('p');
    expect( rbtree.root.left.val ).toBe('m');
    expect( rbtree.root.right.val ).toBe('r');

  })

  /**
   *                   m
   *        e----------+-----------r
   *    ----+----             -----+----
   *    c       l             p        x
   *  ==+--   ==+--                  ==+--
   *  a       h                      s
   */
  it( 'Rbtree::put - s,e,a,r,c,h,x,m,p,l', () =>{
    let rbtree =new Rbtree();
    const keystring ='searchxmpl';
    for (let i = 0; i < keystring.length; i++) {
      let key =keystring[i];
      rbtree.put( key, key);
    }

    // root
    expect( rbtree.root.val ).toBe('m');
    // right sub tree of root
    expect( rbtree.root.right.val ).toBe('r');
    expect( rbtree.root.right.left.val ).toBe('p');
    expect( rbtree.root.right.right.val ).toBe('x');
    expect( rbtree.root.right.right.left.val ).toBe('s');
    // left sub tree of root
    expect( rbtree.root.left.val ).toBe('e');
    // left subtree of e
    expect( rbtree.root.left.left.val ).toBe('c');
    expect( rbtree.root.left.left.left.val ).toBe('a');
    expect( rbtree.root.left.left.right ).toBe(null);
    // right subtree of e
    expect( rbtree.root.left.right.val ).toBe('l');
    expect( rbtree.root.left.right.left.val ).toBe('h');
    expect( rbtree.root.left.right.right ).toBe(null);

  })

  it( 'Rbtree::contains - searchxmpl', () => {
    let rbtree =new Rbtree();
    const keystring ='searchxmpl';
    for (let i = 0; i < keystring.length; i++) {
      let key =keystring[i];
      rbtree.put( key, key);
    }

    expect( rbtree.contains( 'm' )).toBe(true);
    expect( rbtree.contains( 'z' )).toBe(false);
    expect( rbtree.contains( 'h' )).toBe(true);
    expect( rbtree.contains( 's' )).toBe(true);
    expect( rbtree.contains(  null )).toBe(false);
    expect( rbtree.contains( 'z' )).toBe(false);
  })


  it( 'Rbtree::delete(r) - searchxmpl', () => {
    let rbtree = new Rbtree();
    const keystring = 'searchxmpl';
    for (let i = 0; i < keystring.length; i++) {
      let key = keystring[i];
      rbtree.put(key, key);
    }

    rbtree.delete( 'r' );
    expect( rbtree.contains( 'r' )).toBe(false);
  });


  it( 'Rbtree::delete(l) - searchxmpl', () => {
    let rbtree = new Rbtree();
    const keystring = 'searchxmpl';
    for (let i = 0; i < keystring.length; i++) {
      let key = keystring[i];
      rbtree.put(key, key);
    }

    rbtree.delete( 'l' );
    expect( rbtree.contains( 'l' )).toBe(false);
  });

  it( 'Rbtree::delete(m) - searchxmpl', () => {
    let rbtree = new Rbtree();
    const keystring = 'searchxmpl';
    for (let i = 0; i < keystring.length; i++) {
      let key = keystring[i];
      rbtree.put(key, key);
    }

    rbtree.delete( 'm' );
    expect( rbtree.contains( 'm' )).toBe(false);
    expect( rbtree.root.val ).toBe('p');
  });

  it( 'Rbtree::to_list in_order', () => {

      let rbtree =new Rbtree();
      const keystring ='searchxmpl';
      for (let i = 0; i < keystring.length; i++) {
        let key =keystring[i];
        rbtree.put( key, key);
      }
      let list =rbtree.to_list();
      expect( list.length ).toBe( keystring.length );
      expect( list.join(',')).toBe('a,c,e,h,l,m,p,r,s,x');
  });
});

"""

if __name__ == "__main__":
  unittest.main()
