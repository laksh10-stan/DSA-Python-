# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 12:20:25 2010

@author: Lakshmendra Singh
"""

class Node:
    #constructor
    def __init__ (self):
        self.data = None
        self.ptrdiff = None
    #method for setting the data field of the node
    def setData(self,data):
        self.data = data
    #method for getting the data field of the node
    def getData(self):
        return self.data
    #method for setting the pointer difference field of the node
    def setPtrDiff(self, prev, next):
        self.ptrdiff = prev ^ next
    #method for getting the next field of the node
    def getPtrDiff(self):
        return self.ptrdiff