# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 01:58:16 2010

@author: Lakshmendra Singh
"""

#method for inserting a new node at the beginning of the Linked List (at the head)
def insertAtBeginning(self,data):
    newNode = Node()
    newNode.setData(data)
    if self.length == 0:
        self.head= newNode
    else:
        newNode.setNext(self.head)
        self.head = newNode
    self.length += 1