from collections import deque

"""
- create and compute longest chain of connected nodes in a directed graph with cycles.
- the efficient solution uses dynamic programming to store longest path candidates.
"""

class AdjMatrix:
  def __init__(self, *values):
    self.values =values
    self.list_edge =self.create_adj_matrix(values)

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


  # def compute_longest_chain(self):
  #   self.list_edge =self.create_adj_matrix(self.values)
  #   self.map_end_edge_to_longest_chain =dict()
  #
  #   self.compute_list_of_chain_start_that_end_with_chain(None,None, None)
  #   #for idx_of_edge , edge in enumerate(self.list_edge):
  #     #list_chain_that_ends_with_edge_idx =self.compute_list_chain_that_ends_with_edge_idx( idx_of_edge )
  #     #longest_chain_candidate =self.max_chain(list_chain_that_ends_with_edge_idx)
  #     #self.list_chain_of_edge[idx_of_edge] =longest_chain_candidate
  #
  #   # find and return longest chain in self.map_end_edge_to_longest_chain
  #   longest_chain_globally =None
  #   for chain in self.map_end_edge_to_longest_chain.values():
  #     if longest_chain_globally is None:
  #       longest_chain_globally =chain
  #     elif len(chain) > len(longest_chain_globally):
  #       longest_chain_globally =chain
  #
  #   return longest_chain_globally

  def compute_longest_chain_globally(self):
    map_vertex_id_end_to_longest_chain =self.compute_map_vertex_id_end_to_longest_chain()
    longest_chain_globally =None

    for chain in map_vertex_id_end_to_longest_chain.values():
      if longest_chain_globally:
        if len(longest_chain_globally) < len(chain):
          longest_chain_globally =chain
      else:
        longest_chain_globally = chain

    return longest_chain_globally

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





  # def compute_list_chain_that_ends_with_edge_idx(self, idx_of_edge):
  #
  #   list_chain =[]
  #   list_edge =self.shallow_copy_list_exclude_index( self.list_edge, idx_of_edge)
  #   chain =deque( [self.list_edge[idx_of_edge]] )
  #
  #
  #
  #   #   if edge.tail == chain[0].head
  #   #   and :vertex:edge.tail not in chain already
  #   #   then
  #   #     a. chain.appendleft(0, edge)  # push edge to front of chain
  #   #     b. recurse to find next preceding link
  #   #     c. pop
  #   for j, edge_candidate in enumerate(list_edge):
  #     if self.can_connect( edge_candidate, chain ):
  #       chain.appendleft( edge_candidate )
  #       ## recurse
  #       sub_list_edge =self.shallow_copy_list_exclude_index(list_edge, j)
  #       self.compute_list_of_chain_start_that_end_with_chain( chain, sub_list_edge, list_chain)
  #       chain.popleft()
  #
  #   return list_chain

  def compute_map_vertex_id_end_to_longest_chain(self):
    map_vertex_id_end_to_longest_chain =dict()
    for i, edge_candidate in enumerate(self.list_edge):
      chain =deque([edge_candidate])
      sub_list_edge = self.shallow_copy_list_exclude_index(self.list_edge, i)
      self.recurse_compute_map_vertex_id_end_to_longest_chain( chain, sub_list_edge, map_vertex_id_end_to_longest_chain, i )

    # print map_vertex_id_end_to_longest_chain
    for key in map_vertex_id_end_to_longest_chain:
      msg ="{0} ={1}".format( key, map_vertex_id_end_to_longest_chain[key])
      print( msg )

    return map_vertex_id_end_to_longest_chain

  def recurse_compute_map_vertex_id_end_to_longest_chain(self, chain, list_edge, map_longest, i):
    for j, edge_candidate in enumerate(list_edge):
      if self.can_connect(edge_candidate, chain):
        #
        dup_chain =chain.copy()
        dup_chain.appendleft( edge_candidate )
        sub_list_edge =self.shallow_copy_list_exclude_index(list_edge, j )

        # conditionally store dup_chain
        self._conditionally_update_map_longest( map_longest, dup_chain)

        # check for longer chain with same suffix dup_chain
        self.recurse_compute_map_vertex_id_end_to_longest_chain( dup_chain, sub_list_edge, map_longest, i+1)

  @classmethod
  def _conditionally_update_map_longest(cls, map_longest, chain_candidate):
    key_vertex_id_last =chain_candidate[-1][1]
    existing_chain =map_longest.get(key_vertex_id_last, None)
    if existing_chain:
      if len(existing_chain) < len(chain_candidate):
        map_longest[key_vertex_id_last] =chain_candidate
    else:
      map_longest[key_vertex_id_last] =chain_candidate


  # def compute_list_of_chain_start_that_end_with_chain(self, chain=None, list_edge=None, iteration=0):
  #
  #
  #   for i, edge_candidate in enumerate(list_edge):
  #     chain =chain if iteration == 0 else deque([])
  #     list_edge = self.shallow_copy_list_exclude_index(self.list_edge, i)
  #
  #     if len(chain) == 0 :
  #       chain.appendleft(edge_candidate)
  #     elif self.can_connect(edge_candidate, chain):
  #       # then connect and recurse
  #       for j, edge_candidate in list_edge:
  #         chain.appendleft( edge_candidate )
  #         dup_chain =chain.copy()
  #         sub_list_edge =self.shallow_copy_list_exclude_index(list_edge, i)
  #
  #         self.compute_list_of_chain_start_that_end_with_chain(dup_chain, sub_list_edge, iteration+1)
  #         chain.popleft(  )
  #
  #       #end-for-j
  #     #end-if-else
  #
  #     # if at end of list, conditionally add chain to list_chain
  #     if edge_candidate == list_edge[-1]:
  #       # if len(chain) > longest_chain_with_same_edge_tail
  #       # then replace longest_chain_with_same_edge_tail[chain[-1][1] =chain
  #
  #
  #   #end-for-i


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
  longest_chain =adj_matrix.compute_longest_chain_globally()
  print("len(longest_chain) ={0}".format(len(longest_chain)))