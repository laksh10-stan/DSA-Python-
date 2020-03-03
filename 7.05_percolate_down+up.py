# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:03:25 2019

@author: laksh
"""

def perecolateDown(self,i):
    while (i * 2) <= self.size:
        minimumChild = self.minChild(i)
        if self.heapList[i] > self.heapList[minimumChild]:
            tmp = self.heapList[i]
            self.heapList[i] = self.heapList[minimumChild]
            self.heapList[minimumChild] = tmp
    i = minimumChild
def minimumChild(self,i):
    if i * 2 + 1 > self.size:
        return i * 2
    else:
        if self.heapList[i*2] < self.heapList[i*2+1]:
            return i * 2
        else:
            return i * 2 + 1
def percolateUp(self,i):
    while( i // 2 > 0):
        if self.heapList[i] < self.heapList[i // 2]:
            tmp = self.heapList[i // 2]
            self.heapList[i // 2] = self.heapList[i]
            self.heapList[i] = tmp
        i = i // 2
'''
Time Complexity: O(log n). Heap is a complete binary tree and in the worst case we start at the root and come
down to the leaf. This is equal lo the height of the complete binary tree. Space Complexity: O(1).
'''