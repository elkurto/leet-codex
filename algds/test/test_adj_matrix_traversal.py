import unittest
from algds.adj_matrix_traversal import AdjMatrix

class MyTestCase(unittest.TestCase):
  def test_is_edge_tail_same_as_chain_first_head(self):
    adj_matrix = AdjMatrix()
    a =adj_matrix.is_edge_tail_same_as_chain_first_head([1,3], [[3,2],[2,0]])
    self.assertTrue(a)

    a =adj_matrix.is_edge_tail_same_as_chain_first_head([1,3], [[4,2],[2,0]])
    self.assertFalse(a)

  def test_is_edge_head_in_chain(self):
    adj_matrix =AdjMatrix()
    # true bc edge[0] == 1 == chain[-1][1]
    a =adj_matrix.is_edge_head_in_chain([1,3], [[3,0],[0,1]])
    self.assertTrue(a)

    # true bc edge[0] == 1 == chain[2][0]
    a =adj_matrix.is_edge_head_in_chain([1,3], [[3,0],[0,1],[1,9]])
    self.assertTrue(a)

    # false bc edge[0] == 1 is not in {chain[-1][1]==9, chain[0][0]==3, chain[1][0]==0, chain[2][0]==6}
    a =adj_matrix.is_edge_head_in_chain([1,3], [[3,0],[0,6],[6,9]])
    self.assertFalse(a)


  def test_can_connect(self):
    adj_matrix =AdjMatrix()
    # false bc edge[0] == 1 is in chain
    a =adj_matrix.can_connect([1,3], [[3,0],[0,1]])
    self.assertFalse(a)

    # false bc edge[0] == 1 is already in chain
    a =adj_matrix.can_connect([1,3], [[3,0],[0,1],[1,9]])
    self.assertFalse(a)

    # true bc
    #   a. edge[1] == chain[0][0]
    #   b. edge[0] == 1 is not in {chain[-1][1]==9, chain[0][0]==3, chain[1][0]==0, chain[2][0]==6}
    a =adj_matrix.can_connect([1,3], [[3,0],[0,6],[6,9]])
    self.assertTrue(a)




if __name__ == '__main__':
  unittest.main()
