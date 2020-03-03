# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 22:24:39 2019

@author: Lakshmendra Singh
"""

def rangeToList(k):
    result = []
    for i in range(0,k):
        result.append(str(i))
    return result
def baseKStrings(n,k):
    if n == 0: return []
    if n == 1: return rangeToList(k)
    return [ digit+bitstring for digit in baseKStrings(1 ,k)
            for bitstring in baseKStrings(n-1,k)]
print (baseKStrings(4,3))