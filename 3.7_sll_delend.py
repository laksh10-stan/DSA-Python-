# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 02:20:25 2010

@author: Lakshmendra Singh
"""

def deleteLastNodeFromSinglyLinkedList(self):
    if self.length == 0:
        print ("The list is empty")
    else:
        currentnode = self.head
        previousnode = self.head
        while currentnode.getNext() != None:
            previousnode = currentnode
            currentnode = currentnode.gctNext()
        previousnode.setNext(None)
        self.length -= 1