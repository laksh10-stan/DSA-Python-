# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 15:45:54 2019

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
'''
ALTERNATIVE CODING:
```````````````````
'''
def PreorderTraversal(root) :
    P = root
    while(1):
        P = PreorderSuccessor(P)
        if(P == root):
            return
        print (P.data)
'''
Time Complexity: 0(n). Space Complexity: 0(1).
'''