# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 01:57:45 2019

@author: laksh
"""

'''Binary Search Tree Class and its methods'''
class BSTNode:
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None
    #set data
    def setoata(self, data):
        self.data = data
    #get data
    def getData(self):
        return self.data
    #get left child of a node
    def getLeft(self):
        return self.left
    #get right child of a node
    def getRigbt(self):
        return self.right