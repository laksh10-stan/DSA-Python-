# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 03:38:55 2010

@author: Lakshmendra Singh
"""

#Deleting element at given position
def getNode(self, index):
    currentNode = self.head
    if currentNode == None:
        return None
    i = 0
    while i <= index:
        currentNode = currentNode.getNext()
        if currentNode == None:
            break
        i += 1
        return currentNode
def deleteAtGivenPosition(self, index):
    temp = self.getNode(index)
    if temp:
        temp.getPrev.setNext(temp.getNext())
        if temp.getNext():
            temp.getNext().setPrev(temp.getPrev())
        temp.setPrev(None)
        temp.setNext(None)
        temp.setData(None)
#Deleting with given data
def deleteWithData(self, data):
    temp = self.head
    while temp is not None:
        if temp.getData() == data:
        # if it's not the first clement
            if temp.getNext() is not None:
                temp.getNext().setNext(temp.getNext())
                temp.getNext().setPrev(temp.getPrev())
            else:
                #otherwise we have no prev (it's None), head is the next one, and prev becomes None
                self.head = temp.getNext()
                temp.getNext().setPrev(None)
            temp = temp.getNext()

'''
Time Complexity: O(n), for scanning the complete list of size n .
Space Complexity: O(1). for creating one temporary variable.
'''