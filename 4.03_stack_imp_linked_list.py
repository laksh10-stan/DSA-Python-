# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 11:37:03 2019

@author: Lakshmendra Singh
"""

'''
Linked List Implementation
The other way of implementing stacks is by using Linked lists. Push operation is implemented by inserting
clement at the beginning of the list. Pop operation is implemented by deleting the node from the beginning (the
header/top node).
t._4__,__,I •I.___1 s~ -·I.___1 -----'--'I •I. 40___.l___.j+ NU LL
top
'''
#Node of a Singly Linked List
class Node:
    #constructor
    def __init__(self):
        self.data = None
        self.next= None
        #method for setting the data field of the node
    def setData(self, data):
        self.data = data
        #method for getting the data field of the node
    def getData(self):
        return self.data
    #method for setting the next field of the node
    def setNext(self, next):
        self.next = next
        #melhod for getting the next field of the node
    def getNext(self):
        return self.next
        #returns true if the node points to another node
    def hasNext(self):
        return self.next != None
class Stack(object):
    def __init__ (self, data = None):
        self.head = None
        if data:
            for data in data:
                self.push(data)
    def push(self, data):
        temp = Node()
        temp.setData(data)
        temp.setNext(self.head)
        self.head = temp
    def pop(self):
        if self.head is None:
            raise IndexError
        temp = self.head.getData()
        self.head = self.head.getNext()
        return temp
    def peek(self):
        if self.head is None:
            raise IndexError
        return self.head.getData()
our_list = ["first", "second", "third", "fourth"]
our_stack = Stack(our_list)
print (our_stack.pop())
print (our_stack.pop())
'''
Let n be the number of elements in the stack. The complexities for operations with this representation can be
given as:
Space Complexity (for n push operations) 0(n)
Time Complexity of CreateStack() 0(1)
Time Complexity of Push() 0(1) (Average)
Time Complexity of Pop() 0(1)
Time Complexity of Top() 0(1)
Time Complexity of IsEmptyStack() 0(1)
Time Complexity of IsFullStack() 0(1)
Time Complexity of DeleteStack() 0(n)
'''