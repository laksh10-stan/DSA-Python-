# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 02:21:30 2019

@author: laksh
"""

'''
Finding Maximum Element in Binary Search Trees
In BSTs, the maximum element is the right-most node, which does not have right child.
'''
#Search the key from node, iteratively
def findMax(root):
    currentNode = root
    if currentNode.getRight() == None:
        return currentNode
    else:
        return findMax(currentNode.getRight())
'''
Time Complexity: O(n), in worst case (when BST is a right skew tree).
Space Complexity: O(n), for recursive stack.
'''