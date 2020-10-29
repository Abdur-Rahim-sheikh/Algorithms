## Given a graph G, we shall construct a CNF F(G) such that F(G) is satisfiable if G has a Hamiltonian path.
## F(G) has n^2 boolean variables x[i, j] , 1 ≤ i, j ≤ n. Here x[i, j] the ith position in the Hamiltonian path is occupied by node j.

Clauses of our CNF F(G) are as follows:
<b>Assumptions :</b> at first we assume that all node are connected to each other this simplyfies the complexity<br>
then imagine a matrix A<sub>n,n</sub> where each row corresponds to a position of a node to this position complies that<br>
to get hamiltonian path i'th vertex will be node j.
And each columns corresponds to to a vertex/node so for every column/node there is N SAT variable.

1) <b>Each node j must appear in the path:</b> Make clause having all column so to confirm that j'th node has<br>
  to be present at some position at least one.<br>
2) <b>No node j appears twice in the path:</b> Now we make sure that from each column no more than one variable/node is true<br>
  at the same time. By negeting each pair of a column.<br>
  
**Step 1 and 2 confirms that every node have to visit exactly ones.<br>

3) <b>Every position i on the path must be occupied:</b> Make clause having all row so to confirm that i'th position <br>
  is occupied by at least one node.<br>
4) <b>No two nodes j and k occupy the same position in the path: </b> Now we make sure that each row occupied by<br>
  no more than one node.<br>
**Step 3 and 4 confirms that every position of the path has to be occupied by exactly one node.<br>

5) <b>Non-adjacent nodes i and j cannot be adjacent in the path:</b> Finally as at the beginning we assumed that<br>
  every node is connected with each other. so for those edge i to j which are not connected in the graph
  the cannot appear in adjacent position in hamiltonian path.<br>
  So by negeting these edge to be in adjacent position [k,i and k+1,j] we ensure that the path is only possible if <br>
  if all adjacent postioned node has edge to each other.
  
So is complete To SAT convertion.

(rahul-bhati solution)[https://discuss.codechef.com/t/how-to-solve-hamiltonian-path-using-sat-solver-for-undirected-graph/13261/2]
