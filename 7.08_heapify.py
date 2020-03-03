# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:36:00 2019

@author: laksh
"""

def buildHeap(self,A):
    i = len(A) // 2
    self.size = len(A)
    self.heapList = [0] + A[:]
    while (i > 0):
        self.percolateDown(i)
        i = i - 1
'''
Time Complexity: O(log n)
'''