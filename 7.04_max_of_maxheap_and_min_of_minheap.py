# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:51:31 2019

@author: laksh
"""

#Get Maximum for MaxHeap 
def getMaximum(self): 
    if self.size == 0: 
        return  -1 
    return self.heapList[0] 
'''
Time Complexity: O(1).
'''
#Get Minimum for Minheap
def getMinimum(self): 
    if self.size == 0: 
        return  -1 
    return self.heapList[0] 
'''
Time Complexity: O(1).
'''
