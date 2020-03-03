# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 22:20:45 2019

@author: Lakshmendra Singh
"""

def bitStrings(n):
    if n == 0: return []
    if n == 1: return ["O","1"]
    return [digit+bitstring for digit in bitStrings(1)
        for bitstring in bitStrings(n- 1)]
print (bitStrings(4))