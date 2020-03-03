# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 18:45:46 2019

@author: laksh
"""

#Node of a Generic Tree
class TreeNode:
    #constructor
    def __init__ (self, data=None, next=None):
        self.data = data
        self.firstChild = None
        self.secondChild = None