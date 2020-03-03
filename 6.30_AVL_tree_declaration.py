# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 15:40:57 2019

@author: laksh
"""
'''
AVL Tree Declaration
'''
class AVLNode:
    def __init__(self,data,balanceFactor,left,right):
        self.data = data
        self.balanceFactor = 0
        self.left = left
        self.right = right