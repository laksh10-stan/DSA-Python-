# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 03:38:30 2010

@author: Lakshmendra Singh
"""

def getNode(self, index):
    currentNode = self.head
    if currentNode == None:
        return None
    i = 0
    while i < index and currentNode.getNext() is not None:
        currentNode= currentNode.getNext()
        if currentNode == None:
            break
        i += 1
    return currentNode
def insertAtGivenPosition(self, index, data):
    newNode = Node(data)
    if self.head == None or index == 0:
        self.insertAtBeginning(data)
    elif index > 0:
        temp = self.getNode(index)
        if temp == None or temp.getNext() == None:
            self.insert(data)
        else:
            newNode.setNext(temp.getNext())
            newNode.setPrev(temp)
            temp.getNext().setPrev(newNode)
            temp.setNext(newNode)

'''
Time Complexity: O(n). In the worst ense, we may need to insert the node at the end of the list.
Space Complexity: 0(1), for a temporary variable.
'''