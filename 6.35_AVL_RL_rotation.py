# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 16:25:44 2019

@author: laksh
"""

def rightLeftRotate(self, root):
    X = root.right
    if X.balanceFactor == 1:
        root.balanceFactor = 0
        X.balanceFactor = 0
        root=self.singleRightRotate(root)
    else:
        Y = X.left
        if Y.balanceFactor == -1:
            root.balanceFactor = 0
            X.balanceFactor = 1
        elif Y.balanceFactor == 0:
            root.balanceFactor = 0
            X.balanceFactor = 0
        else:
            root.balanceFactor = -1
            X.balanceFactor = 0
        Y.balanceFactor = 0
        root.right = self.singleLeftRotate(X)
        root = self.singleRightRoate(root)
    return root