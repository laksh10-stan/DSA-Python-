# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 02:16:06 2019

@author: laksh
"""
'''
Finding Minimum Element in Binary Search Trees
In BSTs, the minimum element is the left-most node, which does not have left child.
'''
def findMin(root):
    currentNode = root
    if currentNode.getLeft() == None:
        return currentNode
    else:
        return findMin(currentNode.getLeft())
'''
Time Complexity: O(n), in worst case (when BST is a left skew tree).
Space Complexity: O(n), for recursive stack.
'''