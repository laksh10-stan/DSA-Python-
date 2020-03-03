# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 16:17:49 2019

@author: laksh
"""

def InsertRightInInorderTBT(P, Q):
    Q.right = P.right
    Q.RTag = P.RTag
    Q.left = P
    Q.LTag = 0
    P.right = Q
    P.RTag = 1
    if(Q.RTag == 1) :
        Temp = Q.right
        while(Temp.LTag):
            Temp = Temp.left
        Temp.left = Q
'''
Time Complexity: O(n). Space Complexity: 0(1).
'''