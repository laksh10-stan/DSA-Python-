# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 03:38:18 2010

@author: Lakshmendra Singh
"""

def insertAtEnd(self, data):
    if (self.head == None): #To imply that if head ==None
        self.head = Node(data)
        self.tail= self.head
    else:
        current = self.head
        while(current.getNext() != None):
            current = current.getNext()
        current.setNext(Node(data, None, current))
        self.tail = current.getNext()