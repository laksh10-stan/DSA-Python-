# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 02:19:18 2019

@author: laksh
"""

'''
Finding Minimum Element in Binary Search Trees
In BSTs, the minimum element is the left-most node, which does not have left child.
'''
#Non recursive version of the above algorithm can be given as:
def findMin(root):
    currentNode = root
    if currentNode == None:
        return None
    while currentNode.getLeft() !=None:
        currentNode = currentNode.getLeft()
    return currentNode
'''
Time Complexity: O(n). Space Complexity: O(1).
'''