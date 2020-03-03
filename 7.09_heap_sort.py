# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:39:00 2019

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
def pcrcolateUp(self,i):
    while( i // 2 > 0):
        if self.heapList[i] < self.heapList[i // 2]:
            tmp = self.heapList[i // 2]
            self.heapList[i // 2] = self.heapList[i]
            self.heapList[i] = tmp
        i = i // 2
def heapSort(A):
    # convert A to heap
    length = len( A) - 1
    leastParent = length / 2
    for i in range ( leastParent, - 1, -1 ):
        percolateDown( A, i, length )
    # flattenn heap into sorted array
    for i in range (length, 0, -1 ):
        if A[0] > A[i]:
            swap( A, 0, i )
            percolateDown( A, 0, i - 1 )
    #Modfied percolateDown to skip the sorted elements
def percolatenown( A, first, last):
    largest=2*first +1
    while largest <= last:
        # righl child exists and is larger than left child
        if (largest< last) and ( A[largest] < A[largest + 1] ):
            largest+= 1
        #right child is larger than parent
        if A[largest] > A[first]:
            swap( A, largest, first)
            # move down to largest child
            first = largest
            largest = 2 * first + 1
        else:
            return # force exit
def swap( A, x, y):
    temp= A[x]
    A[x] - A[y]
    A[y] - temp
'''
Time complexity: As we remove the clements from the heap, the values become sorted (since maximum elements
are always root only). Since the time complexity of both the insertion algorithm and deletion algorithm is O(log n)
(where n is the number of items in the heap), the time complexity of the heap sort algorithm is O(log n).
'''