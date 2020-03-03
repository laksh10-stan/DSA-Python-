# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 02:11:27 2019

@author: laksh
"""
'''
Non recursive version of the BST search algorithm can be given as:
'''
#Search the key from node, iteratively
def find(root, data):
    currentNode = root
    while currentNode:
        if data == currentNode.getData():
            return currentNode
        if data < currentNode.getData():
            currentNode = currentNode.getLeft()
        else:
            currentNode = currentNode.getRight()
    return None
'''
Time Complexity: O(n). Space Complexity: 0(1).
'''