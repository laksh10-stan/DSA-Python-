# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 15:32:33 2019

@author: laksh
"""

def singleLeftRotate(self,root):
    W = root.left
    root.left = W.right
    W.right = root
    return W
'''
Time Complexity : O(1). Space Complexity: O(1).
'''