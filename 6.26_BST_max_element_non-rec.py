# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 02:25:38 2019

@author: laksh
"""

'''
Finding Maximum Element in Binary Search Trees
In BSTs, the maximum element is the right-most node, which does not have right child.
'''
#Non recursive version of the above algorithm can be given as:
def findMax(root):
    currentNode = root
    if currentNode == None:
        return None
    while currentNode.getRight() == None:
        currentNode = currentNode.getRight()
    return currentNode
'''
Time Complexity: O(n). Space Complexity: O(1).
'''