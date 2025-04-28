from collections import deque

"""
- create and compute longest chain of connected nodes in a directed graph with cycles.
- the efficient solution uses dynamic programming to store longest path candidates.
"""

class AdjMatrix:
  def __init__(self, *values):
    self.values =values
    self.list_edge =self.create_adj_matrix(values)
    self.map_end_edge_to_longest_chain =dict()
    # self.list_chain_of_edge =[] # map of index_of_vertex to a chains that ends with value at index_of_vertex
    #                      # e.g.
    #                      # Given values =[cd, dz, za, ab]
    #                      # Since values[3] =ab then list_chains[3] =[0 (cd), 1 (dz), 2 (za), 3 (ab)]

  def create_adj_matrix(self, values):
    adj_matrix =[]

    for i,si in enumerate(values):
      for j,sj in enumerate(values):
        if i != j and si[-1] == sj[0]:
          adj_matrix.append( (i,j) )

    return adj_matrix

  def print_matrix(self):
    for link in self.list_edge:
      print( "{0} : {1} --> {2}".format( link, self.values[link[0]], self.values[link[1]]))


  def compute_longest_chain(self):
    self.list_edge =self.create_adj_matrix(self.values)
    self.map_end_edge_to_longest_chain =dict()

    for idx_of_edge , edge in enumerate(self.list_edge):

      list_chain_that_ends_with_edge_idx =self.compute_list_chain_that_ends_with_edge_idx( idx_of_edge )
      longest_chain_candidate =self.max_chain(list_chain_that_ends_with_edge_idx)
      self.list_chain_of_edge[idx_of_edge] =longest_chain_candidate


    return self.max_chain(self.list_chain_of_edge)

  def max_chain(self, list_of_chain):
    longest_chain =[]
    for chain in list_of_chain:
      if len(longest_chain) < len(chain):
        longest_chain =chain

    return longest_chain

  def shallow_copy_list_exclude_index(self, list_src, index):
    list_dest =[]
    for i,element in enumerate(list_src):
      if i != index:
        list_dest.append( element )
    return list_dest


  def is_edge_tail_same_as_chain_first_head(self, edge, chain):
    return edge[1] == chain[0][0]

  def is_edge_head_in_chain(self, edge, chain):
    edge_head =edge[0]
    b =edge_head == chain[-1][1]  # is edge_head == chain_last_tail
    if not b:
      for chain_edge in chain:
        b = edge_head == chain_edge[0]
        if b:
          break
    #end-if
    return b

  def can_connect(self, edge, chain):
    predicate_a =self.is_edge_tail_same_as_chain_first_head(edge, chain)
    predicate_b =self.is_edge_head_in_chain(edge, chain)
    return predicate_a and not predicate_b





  def compute_list_chain_that_ends_with_edge_idx(self, idx_of_edge):

    list_chain =[]
    list_edge =self.shallow_copy_list_exclude_index( self.list_edge, idx_of_edge)
    chain =deque( [self.list_edge[idx_of_edge]] )



    #   if edge.tail == chain[0].head
    #   and :vertex:edge.tail not in chain already
    #   then
    #     a. chain.appendleft(0, edge)  # push edge to front of chain
    #     b. recurse to find next preceding link
    #     c. pop
    for j, edge_candidate in enumerate(list_edge):
      if self.can_connect( edge_candidate, chain ):
        chain.appendleft( edge_candidate )
        ## recurse
        sub_list_edge =self.shallow_copy_list_exclude_index(list_edge, j)
        self.compute_list_of_chain_start_that_end_with_chain( chain, sub_list_edge, list_chain)
        chain.popleft()

    return list_chain

    #   if self.can_prefix_edge_to_chain( edge_candidate, chain):
    #
    #     sub_list_edge =self.shallow_copy_list_exclude_index(list_edge, j)
    #     chain.appendleft(edge_candidate)
    #     self.compute_all_chains(chain, sub_list_edge, list_chain )
    #     chain.popleft()
    #
    # return list_chain

  def compute_list_of_chain_start_that_end_with_chain(self, chain, list_edge, list_chain):

    for k, edge_candidate in enumerate(list_edge):
      if self.can_connect( edge_candidate, chain ):
        chain.appendleft( edge_candidate )
        ## recurse
        sub_list_edge =self.shallow_copy_list_exclude_index(list_edge, k)
        self.compute_list_of_chain_start_that_end_with_chain( chain, sub_list_edge, list_chain)
        chain.popleft()

      # if at end of list add chain to list_chain
      if edge_candidate == list_edge[-1]:
        list_chain.append(  chain )
    #end-for-k


  # def compute_all_chains(self, chain, list_edge, list_chain ):
  #   av =self.values
  #   for edge in list_edge:
  #     if edge[1] == chain[-1][0]:  # can connect edge-tail to next-edge-head
  #       pass
  #   return
  #
  # def get_vertex_by_index(self, idx):
  #   return self.values[idx]
  #
  # def vlast(self, idx):
  #   # get the last char/entry in self.values[idx]
  #   return self.get_vertex_by_index(idx)[-1]
  #
  # def vfirst(self, idx):
  #   # get the first char/entry in self.values[idx]
  #   return self.get_vertex_by_index(idx)[0]
  #
  # def can_prefix_edge_to_chain(self, edge_candidate, chain):
  #   b =False
  #
  #   # [last_char_of_candidate == first_char_of_chain
  #   # AND first_char_of_candidate not in chain already
  #   # ]
  #   if self.vfirst(edge_candidate[-1]) == self.vfirst(chain[0][0]): # same vertex in
  #
  #     if edge_candidate[0] != chain[-1][1]:
  #       b =True
  #       for edge_in_chain  in chain:
  #         b =edge_candidate[-1] == edge_in_chain[1]
  #         if not b:
  #           break
  #
  #   return b






if __name__ == "__main__":
  adj_matrix =AdjMatrix("ab", "bc", "bd", "ca", "de", "ef")
  adj_matrix.print_matrix()