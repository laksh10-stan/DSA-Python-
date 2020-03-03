# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:41:56 2019

@author: laksh
"""
'''
Parent of a Node
'''
def parent(self, index):
    return index / 2
'''
Parent will be at math.floor(index/2). Since integer division
simulates the floor function, we don't explicitly use it.
'''
'''   
Time Complexity: O(1).
'''