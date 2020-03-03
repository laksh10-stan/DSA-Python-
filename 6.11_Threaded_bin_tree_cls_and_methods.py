# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 14:43:25 2019

@author: laksh
"""

'''Threaded Binary Tree Class and its methods'''
class ThreadedBinaryTree:
    def __init__(self, data):
        self.data = data           #data
        self.left= None            #left child
        self.LTag = None
        self.right= None           #right child
        self.RTag =None
        
   
'''
Differnce b/w binary tree and Threaded binary tree:
                   Regular Binary Tree              Threaded Binary Tree
if Ltag==0         NULL                             left points to the in-order predecesssor
if Ltag==1         left points to the left child    left points to the left child
if RTag==0         NULL                             right points to the inorder successor
if Rtag==1         right points to the right child  right points to the right child
'''    