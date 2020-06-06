# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 13:49:53 2020
Label-correcting algorithm for shortest paths
@author: Max Fenig
"""
import numpy as np

# label correcting algorithm for finding the shartest path on graph
# g: networkx DiGraph object
# origin: string corresponding to name of origin node
# destination: string corresponding to name of destination node
# copen: data structure for prioritizing search type (see container)
# upperInit: initial worst-case limit on distance from origin to destination
# slack: numeric A* heuristic value, if None, this is ignored
def shortestPath(g, origin, destination, copen, upperInit=np.inf, slack=None):
    # copen is container holding all nodes to be visited stored as tuples
    # (shortest distance to node, node name)
    copen.addNext((0, origin))

    # keep a running tally of shortest distances to all nodes and immediate (best) parent
    # set the origin node distance-to-self (d2s) to 0
    shortest = {origin: {'d': 0, 'parent': None}}
    
    upper = upperInit

    # keep track of all nodes visited
    nodesVisited = [origin]

    # iterate through candidates nodes in copen
    while(copen.numItems > 0):
        # will return a tuple (nodeName, distance2node)
        candidateNode = copen.getNext()        
        for cname in g.successors(candidateNode[1]):
            # distance from parent to child
            a_ij = g.get_edge_data(candidateNode[1], cname)['weight'] 
            # distance to parent
            di = candidateNode[0]
            # left-hand side of equation
            lhs = di + a_ij
            
            # create an A* heuristic here based on children of child
            if slack is not None: 
                # if the next node is destination, then at least 1 from child to destination
                if destination in list(g.successors(cname)):
                    lhs = di + a_ij + 1*slack
                else: # if destination is not next, then there's at least 2 more nodes of non-zero distance
                    lhs = di + a_ij + 2*slack
            else:
                pass # ignore if not provided
            
            # right-hand side 
            if cname in shortest:
                rhs = min(shortest[cname]['d'], upper)
            else:
                rhs = min(np.inf, upper)
                
            if lhs < rhs:
                # set the distance to child as the minimal distance found so far
                dj = di + a_ij # repeated here in case slack is being used
                shortest[cname] = {'d': dj, 'parent': candidateNode[1]}
                if (cname != destination) and (not copen.existsIn(cname)):
                    copen.addNext((dj, cname))
                    nodesVisited.append(cname)
                
                # if the child is the terminal node, then set upper to di + a_ij
                if cname == destination:
                    upper = dj
    
    # this is the shortest path
    minPathLength = shortest[destination]['d']
    
    # generate the path by back-tracking through shortest
    rpath = [destination]
    nextNode = destination
    flag = True
    while(flag):
        nextNode = shortest[nextNode]['parent']
        if nextNode is None:
            flag = False
        else:
            rpath.append(nextNode)
    path = list(reversed(rpath))
    
    return path, minPathLength, nodesVisited