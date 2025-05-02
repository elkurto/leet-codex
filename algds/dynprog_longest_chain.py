from collections import deque

"""
- create and compute longest chain of connected nodes in a directed graph with cycles.
- the efficient solution uses dynamic programming solution to store 
  pre-computed longest path candidates.


usage: 
   
  python3 algds/dynprog_longest_chain.py 

  (0, 1) : ab --> bc
  (0, 2) : ab --> bd
  (1, 3) : bc --> ca
  (2, 4) : bd --> de
  (3, 0) : ca --> ab
  (4, 5) : de --> ef
  0_1 =deque([(3, 0), (0, 1)])
  0_2 =deque([(1, 3), (3, 0), (0, 2)])
  1_3 =deque([(0, 1), (1, 3)])
  2_4 =deque([(1, 3), (3, 0), (0, 2), (2, 4)])
  3_0 =deque([(1, 3), (3, 0)])
  4_5 =deque([(1, 3), (3, 0), (0, 2), (2, 4), (4, 5)])
  len(longest_chain) =6


"""

class FinderLongestChain:
  def __init__(self, *values):
    self.values =values
    self.list_edge =self.create_adj_matrix(values)

  @classmethod
  def create_adj_matrix(cls, values):
    adj_matrix =[]

    for i,si in enumerate(values):
      for j,sj in enumerate(values):
        if i != j and si[-1] == sj[0]:
          adj_matrix.append( (i,j) )

    return adj_matrix

  def print_matrix(self):
    for link in self.list_edge:
      print( "{0} : {1} --> {2}".format( link, self.values[link[0]], self.values[link[1]]))

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

  @classmethod
  def max_chain(cls, list_of_chain):
    longest_chain =[]
    for chain in list_of_chain:
      if len(longest_chain) < len(chain):
        longest_chain =chain

    return longest_chain

  @classmethod
  def shallow_copy_list_exclude_index(cls, list_src, index):
    list_dest =[]
    for i,element in enumerate(list_src):
      if i != index:
        list_dest.append( element )
    return list_dest


  @classmethod
  def is_edge_tail_same_as_chain_first_head(cls, edge, chain):
    return edge[1] == chain[0][0]

  @classmethod
  def is_edge_head_in_chain(cls, edge, chain):
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

        # lookup and conditionally use cached longest map that ends with edge_candidate.
        key =self.convert_edge_to_key(edge_candidate)
        precomputed_longest_chain =map_longest.get(key, None)
        if precomputed_longest_chain and self.can_connect_chain_to_chain( precomputed_longest_chain, chain ):
          # use cached pre-computed longest chain that ends with edge_candidate
          # nb: in this case -- fn does not recurse -- instead use a pre-computed result.
          longest_chain_that_ends_with_edge_candidate  =map_longest.get(key)
          dup_chain =chain.copy()

          for edge in reversed(longest_chain_that_ends_with_edge_candidate):
            dup_chain.appendleft( edge )

          self._conditionally_update_map_longest( map_longest, dup_chain)

        else:
          # nb: in this case -- fn does recurse
          # compute and cache longest chain for first time.
          dup_chain =chain.copy()
          dup_chain.appendleft( edge_candidate )
          sub_list_edge =self.shallow_copy_list_exclude_index(list_edge, j )

          # conditionally store dup_chain
          self._conditionally_update_map_longest( map_longest, dup_chain)

          # check for longer chain with same suffix dup_chain
          self.recurse_compute_map_vertex_id_end_to_longest_chain( dup_chain, sub_list_edge, map_longest, i+1)

  @classmethod
  def can_connect_chain_to_chain(cls, chain_head, chain_tail):

    predicate_a =cls.is_edge_tail_same_as_chain_first_head(chain_head[-1], chain_tail)

    unique_val_in_chain_tail =[x[0] for x in chain_tail]
    unique_val_in_chain_tail.append( chain_tail[-1][1] )

    predicate_b =False
    for edge_in_chain_head in chain_head:
      predicate_b =edge_in_chain_head[0] in unique_val_in_chain_tail
      if predicate_b:
        break

    return predicate_a and not predicate_b



  @classmethod
  def _conditionally_update_map_longest(cls, map_longest, chain_candidate):
    key_edge_at_chain_tail =cls.convert_edge_to_key(chain_candidate[-1])
    existing_chain =map_longest.get(key_edge_at_chain_tail, None)
    if existing_chain:
      if len(existing_chain) < len(chain_candidate):
        map_longest[key_edge_at_chain_tail] =chain_candidate
    else:
      map_longest[key_edge_at_chain_tail] =chain_candidate

  @classmethod
  def convert_edge_to_key(cls, edge):
    return "{0}_{1}".format( edge[0], edge[1])

if __name__ == "__main__":
  finder_longest_chain =FinderLongestChain("ab", "bc", "bd", "ca", "de", "ef")
  finder_longest_chain.print_matrix()
  longest_chain =finder_longest_chain.compute_longest_chain_globally()
  print("len(longest_chain) ={0}".format(len(longest_chain)+1))