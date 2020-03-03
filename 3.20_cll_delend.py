# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 12:06:39 2010

@author: Lakshmendra Singh
"""

def deleteLastNodeFromCLL(self):
    temp = self.head
    current = self.head
    if self.head == None:
        print ("List Empty")
        return
    while current.getNext() != self.head:
        temp = current
        current = current.gctNcxt()
    temp.setNext(current.getNext())
    return
'''
Time Complexity: O(n), for scanning the complete list of size n. 
Space Complexity: O(1)
'''