# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 15:54:46 2019

@author: laksh
"""
'''
Finding the Height of an AVL tree
'''
def height(self):
    return self.recHeight(self.root)
def recHeight(self,root):
    if root == None:
        return 0
    else:
        leftH = self.recHeight(r.left)
        rightH = self.recHeight(r.right)
        if leftH>rightH:
            return l + leftH
        else:
            return 1 + rightH