# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 21:38:14 2019

@author: Lakshmendra Singh
"""

def Fact(num):
    if num == 0:
        return 1
    else:
        return num*Fact(num-1)
print(Fact(6))

        