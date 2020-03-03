# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:11:59 2019

@author: laksh
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:03:25 2019

@author: laksh
"""

def percolateDown(self,i):
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

'''
DELETING AN ELEMENT
```````````````````
'''
#Delete Maximum for MaxHeap
def deleteMax(self):
    retval = self.heapList[1]
    self.heapList[1] =self.heapList[self.size]
    self.size = self.size - 1
    self.heapList.pop()
    self.percolateDown(1)
    return retval 
'''
Time Complexity: O(log n).
'''
#Delete Minimum for MinHeap
def deleteMin(self):
    retval = self.heapList[1]
    self.heapList[1] = self.heapList[self.size]
    self.size = self.size - 1
    self.heapList.pop()
    self.percolateDown(1)
    return retval
'''
Time Complexity: O(log n).
'''

'''
Note : Deleting an element uses PercolateDown, and inserting an element uses PercolateUp.
Time Complexity: same as Heapify function and it is O(log n)
'''