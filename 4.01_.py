# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 11:37:58 2019

@author: Lakshmendra Singh
"""

class Stack(object):
    def __init__ (self, Limit = 10):
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
    our_stack.push{"21")
    our_stack.push("14")
    our_stack.push("31")
    our_stack.push("19")
    our_stack.push("3")
    our_stack.push("99")
    our_stack.push("9")
    print our_stack.peek()
    print our_stack.pop()
    print our_stack.peck()
    print our_stack.pop()