# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 02:07:56 2019

@author: laksh
"""

def find( root, data):
    currentNode = root
    while currentNode is not None and data != currentNode.getData():
        if data> currentNode.getData():
            currentNode = currentNode.getRight()
        else:
            currentNode = currentNode.getLeft()
    return currentNode
'''
Time Complexity: O(n), in worst case (when BST is a skew tree). Space Complexity: O(n), for recursive stack.
'''