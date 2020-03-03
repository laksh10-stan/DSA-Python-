# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 03:37:58 2010

@author: Lakshmendra Singh
"""

def insertAtBeginning(self, data):
    newNode = Node(data, None, None)
    if (self.head == None): #To imply that if head ==None
        self.head = self.tail = newNode
    else:
        newNode.setPrev(None)
        newNode.setNext(self.head)
        self.head.setPrev(newNode)
        self.head = newNode