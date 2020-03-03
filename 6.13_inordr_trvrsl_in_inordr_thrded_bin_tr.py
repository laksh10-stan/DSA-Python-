# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 15:26:55 2019

@author: laksh
"""
'''
We can start with dummy node and call InorderSucccssor() to visit each node until we reach dummy node.
'''
def InorderSuccessor(P):
    if(P.RTag == 0):
        return P.right
    else:
       Position = P.right
       while(Position.LTag == 1):
            Position = Position.left
            return Position
def Inordertraversal(root):
    P = InorderSuccessor(root)
    while(P != root):
        P = InorderSuccessor(P)
        print (P.data)
'''
Time Complexity: O(n). Space Compkxity: 0(1).
'''