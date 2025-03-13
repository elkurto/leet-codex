import unittest
import enum


def compareKeyFnDefault( a, b):
	rval =0
	if a < b:
		rval =-1
	elif a > b:
		rval = 1
	return rval


class Color(enum.Enum):
	RED =True
	BLACK =False


class Node(object):
	def __init__(self,key, value):
		self.key =key
		self.value =value
		self.left =None  # left child
		self.right =None # right child
		self.color =Color.BLACK

	# def make_black(self):
	# 	self.color =Color.BLACK
	#
	# def make_red(self):
	# 	self.color =Color.RED
	#
	# def is_black(self):
	# 	return self.color is Color.BLACK
	#
	# def is_red(self):
	# 	return self.color is Color.RED
	#
	# def size(self):
	# 	return self.N
	
#end-def	


class Rbtree(object):
	"""
		- Red links lean left.
		- No node has two red links connected to it.
		- The tree has perfect black balance: every path from the root to a null link has the same number of black links. 
	"""
	def __init__(self, compareKeyFn=None):
		self.root =None
		self.compareKeyFn =compareKeyFn if compareKeyFn else compareKeyFnDefault

	def is_red(self, node):
		return node and node.color is Color.RED

	def get(self, key):
		return self._get(key, self.root )

	def _get(self, key, h ):
		if h is None:
			pass # no match
		else:
			icmp =self.compareKeyFn( key, h.key)
			if icmp == 0 :
				pass # key == h.key , then key found so return h
			elif icmp < 0:
				h =self._get(key, h.left)
			elif icmp > 0:
				h =self._get(key, h.right)
			#endif
		return h

	def contains(self, key):
		if key is None :
			return False

		return self.get(key) is not None

	def put(self, key, val ):

		h =self.root
		self.root =self._put( h, key, val)
		self.root.color =Color.BLACK

	def _put(self, h, key , val ):
		if h is None:
			rbnode =Node(key,val)
			rbnode.color =Color.RED
			return rbnode


		icmp =self.compareKeyFn( key, h.key )

		if icmp == 0 : # ,then key already exists, so replace h.val and return null
			h.val =val
		elif icmp < 0 :
			h.left =self._put(h.left, key,val)
		elif icmp > 0 :
			h.right =self._put(h.right, key, val )


		# fix-up any right leaning links and return new h to ascend recursively
		if (not self.is_red(h.left)) and self.is_red(h.right) :
			h =self._rotate_left(h)

		if self.is_red(h.left) and self.is_red(h.left.left):
			h =self._rotate_right(h)

		if self.is_red( h.left) and self.is_red( h.right):
			self._flip_color(h)

		return h



	def _rotate_right(self, h):
		"""
		"""
		x =h.left
		h.left =x.right
		x.right =h
		x.color =h.color
		h.color =Color.RED # ??? this assumes that initially h.left is RED

		return x 
		
	def _rotate_left(self, h):
		"""
		"""
		x =h.right
		h.right =x.left
		x.left =h
		x.color =h.color
		h.color =Color.RED  # ??? this assumes that initially h.right is RED

		return x
	
	def _flip_color(self, h):
		h.color =Color.RED
		h.left.color =Color.BLACK
		h.right.color =Color.BLACK

	



class Test_Rbtree(unittest.TestCase):

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
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()
	