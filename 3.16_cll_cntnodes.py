# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 11:33:32 2010

@author: Lakshmendra Singh
"""

#This method would be a member of other class (say, CircularList)
def circularListLength(self):
    currentNode = self.head
    if currentNode == None:
        return 0
    count = 1
    currentNode = currentNode.getNext()
    while currentNode != self.head:
        currentNode = currentNode.getNext()
        count = count + 1
    return count

'''
Time Complexily: O(n), for scanning the complete list of size n. 
Space Complexity: 0(1), for temporory variable.
'''