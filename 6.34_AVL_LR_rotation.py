# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 16:13:36 2019

@author: laksh
"""

def rightLeftRotate(self, root):
    X = root.left
    if X.balanceFactor == - 1:
        root.balanceFactor = 0
        X.balanceFactor = 0
        root = self.singleLeftRotate(root)
    else:
        Y = X.right
    if Y.balanceFactor == - 1:
        root.balanceFactor = 1
        X.balanceFactor = 0
    elif Y.balanccFactor == 0:
        root.balanceFactor = 0
        X.balanceFactor = 0
    else:
        root.balanceFactor = 0
        X.balanceFactor = -1
        Y.balanceFactor = 0
        root.left = self.singleRightRoatate(X)
        root = self.singleLeftRotate(root)
    return root