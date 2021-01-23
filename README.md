An implementation of the label-correcting algorithm utilizing networkx. 
This method is a generalized algorithm for shortest paths that treats breadth-first, depth-first, best-first, and 
best-first with heuristic (A*) search algorithms as special cases contingent on a "container" object for storing and prioritizing 
nodes and a heuristic parameter.  The container-to-search algorithm mappings are:


queue: breadth-first

stack: depth-first

best-first: priority queue

best-first with heuristic: priority queue (and a heuristic parameter as input)

See Section 2.3 of Bertsekas, Dimitri P. Dynamic Programming and Optimal Control, Volume I. 4th ed. Athena Scientific, 2017
