# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 15:19:39 2020
Container data structure for use in label-correcting algorithm
@author: Max Fenig
"""
from abc import ABCMeta, abstractmethod
from collections import deque
import heapq

# abstract class for storing nodes to be visited
class container(object):
    __metaclass__ = ABCMeta
    def __init__(self):
        # keeps track of number of items
        self.numItems = 0
        # keeps track of unique items
        self.setc = set([])
    
    @abstractmethod
    def addNext(self):
        pass

    @abstractmethod
    def getNext(self):
        pass
    
    @abstractmethod
    def existsIn(self, testItem):
        pass

# stack
class stack(container):
    
    def __init__(self):
        super(stack, self).__init__()
        self.stack = []
        
    def getNext(self):
        nextItem = self.stack.pop()
        self.setc.remove(nextItem)
        self.numItems -= 1
        return nextItem
    
    def addNext(self, newItem):
        self.setc.add(newItem)
        self.stack.append(newItem)
        self.numItems += 1
    
    def existsIn(self, testItem):
        return testItem in self.setc
    
# queue
class q(container):
    
    def __init__(self):
        super(q, self).__init__()
        self.q = deque([])
        
    def getNext(self):
        nextItem = self.q.popleft()
        self.setc.remove(nextItem)
        self.numItems -= 1
        return nextItem
    
    def addNext(self, newItem):
        self.q.append(newItem)
        self.setc.add(newItem)
        self.numItems += 1
            
    def existsIn(self, testItem):
        return testItem in self.setc
    
# priority queue
class pq(container):
    
    def __init__(self):
        super(pq, self).__init__()
        self.pq = []
        
    def getNext(self):
        nextItem = heapq.heappop(self.pq)
        self.setc.remove(nextItem)
        self.numItems -= 1
        return nextItem
    
    
    def addNext(self, newItem):
        heapq.heappush(self.pq, newItem)
        self.numItems += 1
        self.setc.add(newItem)
    
    def existsIn(self, testItem):
        return testItem in self.setc