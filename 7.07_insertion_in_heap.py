# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:25:52 2019

@author: laksh
"""

def insert(self,k):
    self.heapList.append(k)
    self.size = self.size + 1
    self.percolateUp(self.size)
'''
Time Complexity: O(logn). The expla nulion is the same as that of the lleapify func tion.
'''