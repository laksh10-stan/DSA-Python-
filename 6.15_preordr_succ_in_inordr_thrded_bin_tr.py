# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 15:45:52 2019

@author: laksh
"""

'''
Finding PreOrder Successor in InOrder Threaded Binary Tree
Strategy: If P has a left subtree, then return the left child of P. If P has no left subtree, then return the right
child of the nearest node whose right subtree contains P.
'''
def PreorderSuccessor(P):
    if(P.LTag == 1):
        return P.left
    else:
        Position = P
        while(Position.RTag == 0):
            Position = Position.right
            return Position.right
'''
Time Complex ity: O(n). Space Complexity: 0(1).
'''