# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 02:18:49 2010

@author: Lakshmendra Singh
"""

#method to delete the first node of the linked list
def deleteFromBeginnjng(self):
    if self.length == 0:
        print("The list is empty")
    else:
        self.head = self.head.getNext()
        self.length -= 1