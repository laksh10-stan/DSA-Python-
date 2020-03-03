# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 22:36:38 2019

@author: Lakshmendra Singh
"""

def listLength(self):
    current= self.head
    count= 0
    while current != None:
        count = count+ 1
        current= current.getNext()
        return count

'''
Time Complexity: O(n), for scanning the list of size n.
Space Complexity: 0(1), for creating a temporary variable.
'''