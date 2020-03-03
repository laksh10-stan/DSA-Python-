# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 21:44:33 2019

@author: Lakshmendra Singh
"""

def Print(n):
    if n == 0: # this is lhe terminating base case
        return 0
    else:
        print (n)
        return Print(n-1)
print(Print(4))