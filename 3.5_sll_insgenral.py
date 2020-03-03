# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 02:06:16 2010

@author: Lakshmendra Singh
"""

#Method for inserting a new node a t a ny position in a Linked List
def insertAtPos(self,pos,data):
    if pos > self.length or pos < 0:
        return None
    else:
        if pos == 0:
            self.insertAtBeg(data)
        else:
            if pos == self.length:
                self.insertAtEnd(data)
            else:
                newNode = Node()
                newNode.setData(data)
                count = 0
                current= self.head
                while count< pos-1:
                    count+= 1
                    current = current.getNext()
                newNode.setNext(current.getNext())
                current.setNext(newNode)
                self.length += 1
                
'''
Time Complexity: O(n), since, in the worst case, we may need to insert the node at the end of the list.
Space Complexity: O(1), for creating one temporary variable.
'''