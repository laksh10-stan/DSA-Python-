# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 02:28:34 2010

@author: Lakshmendra Singh
"""

#Delete with node from linked list
def deleteFromLinkedListWithNode(self, node):
    if self.length == 0:
        raise ValueError("List is empty")
    else:
        current=self.head
        previous = None
        found = False
        while not found:
            if current == node:
                found = True
            elif current is None:
                raise ValueError("Node not in Linked List")
            else:
                previous = current
                current=current.getNext()
    if previous is None:
        self.head = current.getNext()
    else:
        previous.setNext(current.getNext())
    self.length -= 1
#Delete with data from linked list
def deleteValue(self, value):
    currentnode = self.head
    previousnode = self.head
    while currentnode.next != None or currentnode.value !=value:
        if currentnode.value == value:
            previousnode.next = currentnode.next
            self.length -= 1
            return
        else:
            previousnode = currentnode
            currentnode = currentnode.next
            print ("The value provided is not present")
#Method lo delete a node al a particular position
def deleteAtPosition(self,pos):
    count = 0
    currentnode =self.head
    previousnode = self.head
    if pos > self.length or pos < 0:
        print( "The position does not exist. Please enter a valid position")
    else:
        while currentnode.next != None or count < pos:
            count = count + 1
            if count == pos:
                previousnode.next = currentnode.next
                self.length -= 1
                return
            else:
                previousnode = currentnode
                currentnode = currentnode.next
                
'''
Time Complexity: 0(n). In the worst case, we may need to delete the node at the end of the list.
Space Complexity: 0(1), for one temporary variable.
'''