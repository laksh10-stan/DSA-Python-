# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 16:33:25 2019

@author: laksh
"""

def insert(self,data):
    newNode = AVLNode(data,O,None,None)
    [self.root, taller] = self.recInsertAVL(self.root1, newNode)
def recInsertAVL(self, root, newNode):
    if root == None:
        root = newNode
        root.balanceFactor = 0
        taller = True
    elif newNode.data< root.data:
        [root.left, taller] = self.recInsertAVL(root.left, newNode)
        if taller:
             if root.balanceFactor == 0 :
                 root.balanceFactor = -1
             elif root.balanceFactor == 1:
                 root.balanceFactor= 0
                 taller = False
        else :
            root= self.rightLeftRotate(root)
            taller = False    
    else:
        [root.right, taller] = self.recInsertAVL(root.right, newNode)
    if taller:
        if root.balanceFactor == -1:
            root.balanceFactor = 0
            taller = False
    elif root.balanceFactor == 0 :
        root.balanceFactor = 1
    else:
        root = self.rightLeftRotate(root)
        taller = False
    return [root,taller]
'''
Time Complexity: O(logn). Space Complexity: O(logn).
'''