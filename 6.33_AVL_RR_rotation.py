# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 16:03:01 2019

@author: laksh
"""

def singleRightRotate(self,root):
    X = root.right
    root.right= X.left
    X.left = root
    return X
'''
Time Complexity: O(1). Space Complexity: O(1).
'''