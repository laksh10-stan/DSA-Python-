# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 15:27:08 2019

@author: laksh
"""
'''
We can start with dummy node and call InorderSucccssor() to visit each node until we reach dummy node.
'''
'''
ALTERNATIVE CODE:
``````````````````
'''
def InorderSuccessor(P):
    if(P.RTag == 0):
        return P.right
    else:
       Position = P.right
       while(Position.LTag == 1):
            Position = Position.left
            return Position
def InorderTraversal(root):
    P = root
    while(1):
        P = InorderSuccessor(P)
        if(P == root):
            return
        print (P.data)
'''
Time Complexity: O(n). Space Compkxity: 0(1).
'''