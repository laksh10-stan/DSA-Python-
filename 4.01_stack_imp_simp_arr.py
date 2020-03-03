# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 11:37:58 2019

@author: Lakshmendra Singh
"""
'''
Simple Array Implementation

This implementation of stack ADT uses an array. In the array, we add elements from left to right and use a
variable to keep track of the index of the top element.

The array storing the stack elements may become full. A push operation will then throw a full stack exception.
Similarly, 1f we try deleting an element from an empty stack it will throw stack empty exception.
'''

class Stack(object):
    def __init__ (self, limit = 10):
        self.stk = []
        self.limit = limit
    def isEmpty(self):
        return len(self.stk) <= 0
    def push(self, item):
        if len(self.stk) >= self.limit:
            print ('Stack Overflow!')
        else:
            self.stk.append(item)
        print ('Stack after Push',self.stk)
    def pop(self):
        if len(self.stk) <= 0:
            print ('Stack Underflow!')
            return 0
        else:
            return self.stk.pop()
    def peek(self):
        if len(self.stk) <= 0:
             print ('Stack Underflow')
             return 0
        else:
             return self.stk[-1]
    def size(self):
        return len(self.stk)
our_stack = Stack(5)
our_stack.push("1")
our_stack.push("21")
our_stack.push("14")
our_stack.push("31")
our_stack.push("19")
our_stack.push("3")
our_stack.push("99")
our_stack.push("9")
print (our_stack.peek())
print (our_stack.pop())
print (our_stack.peek())
print (our_stack.pop())

'''
Let n be the number of elements in the stack. The complexities of stack operations with this representation can
be given as:
Space Complexity (for n push operations) 0(n)
Time Complexity of Push() 0(1)
Time Complexity of Pop() 0(1)
Time Complexity of Size() 0(1)
Time Complexity of IsEmptyStack() 0(1)
Time Complexity of IsFullStack() 0(1)
Time Complexity of DeleteStack() 0(1)
Limitations
The maximum size of the stuck must first be defined und it cannot be changed. Trying to push a new element
into a full stack causes an implementation-specific exception.
'''