import unittest
import enum


def compare_key_fn_default(a, b):
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
	def __init__(self, compare_key_fn=None):
		self.root =None
		self.compare_key_fn =compare_key_fn if compare_key_fn else compare_key_fn_default

	@classmethod
	def is_red(cls, node):
		return node and node.color is Color.RED

	def get(self, key):
		return self._get(key, self.root )

	def _get(self, key, h ):
		if h is None:
			pass # no match
		else:
			icmp =self.compare_key_fn(key, h.key)
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


		icmp =self.compare_key_fn(key, h.key)

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
			self._flip_colors(h)

		return h


	"""
	*               S=h                      E=x
	*           +---+---+      -->       +---+------+
	*           |       |                |          |
	*           E=x     gtS              ltE        S=h
	*       +---+---+                           +-------+
	*      ltE     gtE_ltS                   gtE_ltS   gtS
	*
	*      0. x =h.left
	*      1. h.left swaps x for gtE_ltS   (ie h takes middle_subtree from x)
	*      2. x.right swaps gtE_ltS for h  (ie x becomes new parent)
	"""
	@classmethod
	def _rotate_right(cls, h):
		"""
		"""
		x =h.left
		h.left =x.right
		x.right =h
		x.color =h.color
		h.color =Color.RED # ??? this assumes that initially h.left is RED

		return x

	"""
	*          E=h                               S=x
	*      +---+------+                      +---+---+
	*      |          |         -->          |       |
	*      ltE        S=x                    E=h     gtS
	*             +-------+              +---+---+
	*          gtE_ltS   gtS            ltE     gtE_ltS
	*
	*
	*      0. x =h.right
	*      1. h.right swaps x for gtE_ltS   (ie h takes middle_subtree from x)
	*      2. x.left swaps gtE_ltS for h    (ie x becomes new parent)
	"""
	@classmethod
	def _rotate_left(cls, h):
		"""
		"""
		x =h.right
		h.right =x.left
		x.left =h
		x.color =h.color
		h.color =Color.RED  # ??? this assumes that initially h.right is RED

		return x

	@classmethod
	def _flip_colors(cls, h):
		h.color =Color.RED
		h.left.color =Color.BLACK
		h.right.color =Color.BLACK

	def is_empty(self):
		return self.root is None


	def delete( self, key ):
		if key is None:
			return

		if not self.contains(key):
			return

		if not self.is_red(self.root.left) and not self.is_red(self.root.right):
			self.root.color =Color.RED


		self.root =self._delete( self.root, key )
		if not self.is_empty():
			self.root.color =Color.BLACK

	# delete the key-value pair with the minimum key rooted at h
	def _delete_min(self, h):
		if h.left is None:
			return None

		if not self.is_red(h.left) and not self.is_red(h.left.left):
			h = self._move_red_left(h)

			h.left = self._delete_min(h.left)
			return self._balance(h)

	# return the node with the minimum key in subtree, x
	def _min( self, x ):

		if x.left is None:
			min_node =x
		else:
			min_node =self._min(x.left)

		return min_node

	# delete the key-value pair with the given key rooted at h
	def _delete(self, h, key ):
		# assert get(h, key) != null;

		if self.compare_key_fn(key, h.key) < 0:
			if not self.is_red(h.left) and not self.is_red(h.left.left):
				h = self._move_red_left(h)

			h.left = self._delete(h.left, key) # keep searching

		else:
			if self.is_red(h.left):
				h = self._rotate_right(h)

			if self.compare_key_fn(key, h.key) == 0 and h.right is None:
				return None

			if not self.is_red(h.right) and not self.is_red(h.right.left):
				h = self._move_red_right(h)

			if self.compare_key_fn(key, h.key) == 0:
				x = self._min(h.right)
				h.key = x.key
				h.val = x.val

				h.right = self._delete_min(h.right)
			else:
					h.right = self._delete(h.right, key)

		return self._balance(h)
	# end-fn _delete

	# Assuming that h is red and both h.left and h.left.left
	# are black, make h.left or one of its children red.
	def _move_red_left(self, h):
		# assert (h != null);
		# assert isRed(h) && !isRed(h.left) && !isRed(h.left.left);

		self._flip_colors(h)
		if self.is_red(h.right.left):
			h.right = self._rotate_right(h.right)
		h = self._rotate_left(h)
		self._flip_colors(h)

		return h

	# Assuming that h is red and both h.right and h.right.left
	# are black, make h.right or one of its children red.
	def _move_red_right(self, h):
		# assert (h != null);
		# assert isRed(h) && !isRed(h.right) && !isRed(h.right.left);
		self._flip_colors(h)
		if self.is_red(h.left.left):
			h = self._rotate_right(h)
			self._flip_colors(h)

		return h

	# restore red-black tree invariant
	def _balance( self, h):
		# assert (h != null);

		if self.is_red(h.right) and not self.is_red(h.left):
			h = self._rotate_left(h)

		if self.is_red(h.left) and self.is_red(h.left.left):
			h = self._rotate_right(h)

		if self.is_red(h.left) and self.is_red(h.right):
			self._flip_colors(h)

		return h

	def to_list(self):
		values =[]
		self._to_list(self.root, values)

		return values


	def _to_list( self, h , values):
		if h is None:
			return

		self._to_list( h.left, values )
		values.append( h.val )
		self._to_list( h.right, values )


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
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()
	