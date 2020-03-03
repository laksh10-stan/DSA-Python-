# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 21:59:58 2019

@author: Lakshmendra Singh
"""

def isArrayInSortedOrder(A):
#Base case
    if len(A) == 1:
        return True
    return A[0] <= A[1] and isSorted(A[1:])
A= [127, 220, 246, 277, 321, 454, 534, 565, 933]
print(isArrayInSortedOrder(A))