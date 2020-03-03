# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 15:45:53 2019

@author: laksh
"""

def PreorderSuccessor(P):
    if(P.LTag == 1):
        return P.left
    else:
        Position = P
        while(Position.RTag == 0):
            Position = Position.right
            return Position.right
'''
PreOrder Traversal of InOrder Threaded Binary Tree
As in inorder traversal, start with dummy node and call PreorderSuccessor() to visit each node until we get
dummy node again.
'''
def PreorderTraversal(root):
    P = PreorderSuccessor(root)
    while(P != root) :
        P = PreorderSuccessor(P)
        print (P.data)
'''
Time Complexity: 0(n). Space Complexity: 0(1).
'''