# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 11:57:41 2010

@author: Lakshmendra Singh
"""

def insertAtBeginInCLL (self, data):
    current = self.head
    newNode = Node()
    newNode.setData(data)
    while current.getNext != self.head:
        current = current.getNext()
    newNode.setNext(newNode)
    if self.head== None:
         self.head = newNode
    else:
        newNode.setNext(self.head)
        current.setNext(newNode)
        self.head = newNode
'''
Time Complexity: O(n), for scanning the complete list of size n.
 Space Complexity: O(1), for temporary variable.
'''