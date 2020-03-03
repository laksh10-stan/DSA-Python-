# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:44:43 2019

@author: laksh
"""

def leftChild(self, index):
    """ 1 is added because array begins at index 0 """
    return 2 * index + 1
'''
Time Complexity: O(1).
'''
def rightChild(self, index):
    return 2 * index + 2
'''
Time Complexity: O(1).
'''