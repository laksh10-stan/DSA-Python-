# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 15:26:35 2019

@author: laksh
"""
'''
To find inorder successor of a given node without using a stack, assume that the node for which we want to find
the inorder successor is P.
Strategy: If P has a no right subtree, then return the light child of P. If P has right subtree, then return the left
of the nearest node whose left subtree contains P.
'''
def InorderSuccessor(P):
    if(P.RTag == 0):
        return P.right
    else:
       Position = P.right
       while(Position.LTag == 1):
            Position = Position.left
            return Position
'''
Time Complexity: O(n). Space Complexity: 0(1).
'''