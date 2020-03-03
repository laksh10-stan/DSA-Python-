# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 02:02:36 2010

@author: Lakshmendra Singh
"""

#method for inserting a new node at the end of a Linked List
def insertAtEnd(self,data):
    newNode= Node()
    newNode.setData(data)
    current= self.head
    while current.getNext() != None:
        current = current.getNext()
    current.setNext(newNode)
    self.length+=1