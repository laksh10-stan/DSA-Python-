# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 11:42:40 2010

@author: Lakshmendra Singh
"""

def printCircularList(self):
    currentNode = self.head
    if currentNode == None:
        return 0
    print (currentNode.getData())
    currentNode = currentNode.getNext()
    while currentNode != self.head:
        currentNode = currentNode.getNext()
        print (currentNode.getData())

'''
Time Complexity: O(n), for scanning the complete list of size n.
Space Complexity: O(1), for temporary variable.
'''