# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 15:44:43 2019

@author: Lakshmendra Singh
"""

class Queue(object):
    def __init__(self,limit = 5):
        self.que = []
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0
    def isEmpty(self):
        return self.size <= 0
    def enQueue(self,item):
        if self.size >= self.limit:
            print ('Queue Overflow!')
            return
        else:
            self.que.append(item)
            
        if self.front is None:
            self.front = self.rear= 0
        else:
            self.rear = self.size
        self.size += 1
        print ('Queue after enQueue',self.que)
    def deQueue(self):
        if self.size <= 0:
             print ('Queue Underflow')
             return 0
        else:
            self.que.pop(0)
            self.size -=1
            if self.size == 0:
                self.front= self.rear = None
            else:
                self.rear = self.size - 1
            print ('Queue after deQueue',self.que)
    def queueRear(self):
        if self.rear is None:
            print ("Sorry, the queue is empty!")
            raise IndexError
        return self.que[self.rear]
    def queueFront(self):
        if self.front is None:
            print ("Sorry, the queue is empty")
            raise IndexError
        return self.que[self.front]
    def size(self):
        return self.size
que = Queue()
que.enQueue("first")
print ("Front: "+que.queueFront())
print ("Rear: "+que.queueRear())
que.enQueue("second")
print ("Front: "+que.queueFront())
print ("Rear: "+que.queueRear())
que.enQueue("third")
print ("Front: "+que.queueFront())
print ("Rear: "+que.queueRear())
que.deQueue()
print ("Front: "+que.queueFront())
print ("Rear: "+que.queueRear())
que.deQueue()
print ("front: "+que.queueFront())
print ("Rear: "+que.queueRear()) 
'''
Performance: Let n be the number of elements in the queue:
Space Complexity for n EnQueue operations --> O(n)
Time Complexity of EnQueue()              --> O(1)
Time Complexity of DeQueue()              --> O(1)
Time Complexity of IsEmptyQueue()         --> O(1)
Time Complexity of IsFullQueue()          --> O(1)
Time Complexity of QueueSize()            --> O(1)
Time Complexity of DeleteQueue()          --> O(1)

Limitations: The maximum size of the queue must be defined as prior and cannot be changed.
Trying to EnQueque a new element into a full queue causes an implementation-specific exception.
'''       