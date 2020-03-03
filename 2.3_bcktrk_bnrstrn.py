# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 22:11:38 2019

@author: Lakshmendra Singh
"""

def appendAtBeginningFront(x, L):
    return [x + element for element in L]
def bitStrings(n):
    if n == 0: return []
    if n == 1: return ["0","1"]
    else:
        return (appendAtBeginningFront("0", bitStrings(n-1)) + appendAtBeginningFront(" 1", bitStrings(n-1 )))
print (bitStrings(4))