# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 15:17:08 2020
Tests for label-correcting algorithm
@author: Max Fenig
"""
import unittest
import networkx
import container
import labelCorrect as lc

# TSP graph (see Sec. 2.3 of Bertsekas)
def createExample():    
    DG = networkx.DiGraph()
    edgeList = [('A', 'AB', 5), ('AB', 'ABC', 20), ('ABC', 'ABCD', 3), ('ABCD', 'T', 15),\
                ('AB', 'ABD', 4), ('ABD', 'ABDC', 3), ('ABDC', 'T', 1),\
                ('A', 'AC', 1), ('AC', 'ACB', 20), ('ACB', 'ACBD', 4), ('ACBD', 'T', 15),\
                ('AC', 'ACD', 3), ('ACD', 'ACDB', 4), ('ACDB', 'T', 5),\
                ('A', 'AD', 15), ('AD', 'ADB', 4), ('ADB', 'ADBC', 20), ('ADBC', 'T', 1),\
                ('AD', 'ADC', 3), ('ADC', 'ADCB', 20), ('ADCB', 'T', 5)]
    DG.add_weighted_edges_from(edgeList)
    return DG

# tests
class lcTests(unittest.TestCase):
    
    def testContainers(self):
        exampleStack = container.stack()
        exampleStack.addNext((0, 's0'))
        exampleStack.addNext((0, 's1'))
        exampleStack.addNext((0, 's2'))
        self.assertTrue(exampleStack.getNext()[1] == 's2')

        exampleq = container.q()
        exampleq.addNext((1, 'q0'))
        exampleq.addNext((2, 'q0'))
        exampleq.addNext((3, 'q0'))
        self.assertTrue(exampleq.getNext()[0] == 1)
        
        examplepq = container.pq()
        examplepq.addNext((1, 'b'))
        examplepq.addNext((0, 'a'))
        examplepq.addNext((2, 'c'))
        self.assertTrue(examplepq.getNext()[0] == 0)
        
    # test label-correction
    def testLC(self):
        g = createExample()
        
        # use a queue (breadth-first)
        pBFS, mplBFS, nvBFS = lc.shortestPath(g, 'A', 'T', container.q())
        self.assertTrue(len(nvBFS) == 16)
        
        # use a stack (depth-first)
        pDFS, mplDFS, nvDFS = lc.shortestPath(g, 'A', 'T', container.stack())
        self.assertTrue(len(nvDFS) == 13)
        
        # use a priority q (best-first)
        pBest, mplBest, nvBest = lc.shortestPath(g, 'A', 'T', container.pq())
        self.assertTrue(len(nvBest) == 10)
        
        # best-first with heuristic/A*
        pA, mplA, nvA = lc.shortestPath(g, 'A', 'T', container.pq(), slack=1)
        self.assertTrue(len(nvA) == 9)
        
if __name__ == '__main__':
    unittest.main()