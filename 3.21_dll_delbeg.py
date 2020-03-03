# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 12:14:15 2010

@author: Lakshmendra Singh
"""

def deleteFrontNodeFromCLL (self):
    current = self.head
    if self.head == None:
        print ("List Empty")
        return
    while current.getNext() != self.head:
        current = current.getNext()
    current.setNext(self.head.getNext())
    self.head = self.head.getNext()
    return
'''
Time Complexity: O(n), for scanning the complete list of size n. 
Space Complexity: O(1)
'''