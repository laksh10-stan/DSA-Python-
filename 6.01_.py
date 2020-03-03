# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 15:40:51 2019

@author: Lakshmendra Singh
"""

'"Binary Tree Class and its methods"'
class BinaryTreeNode:
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right - None
        #set data
    def setData(self, data):
        self.data = data
        #get data
    def getData(self):
        return self.data
        #Igel left child of a node
    def getLeft(self):
        return self.left
        #get right child of a node
    def getRight(self):
        return self.right