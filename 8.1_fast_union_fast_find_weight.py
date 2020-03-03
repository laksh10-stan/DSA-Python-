# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 23:59:57 2019

@author: laksh
"""
#MAKESET
class DisjointSet:
    def __init__ (self, n):
        self.MAKESET(n)
    def MAKESET(self, n):
        self.S =[-1 for x in range(n)]
#FIND
def FIND(self, X):
    if( S[X] < 0):
        return X
    else:
        return self.FIND(self.s[X])
#UNION

def UNION(self, root1, root2):
    if self.FIND(root1) == self.FIND(root2) and self.FIND(root1) == -1 :
        return
    if(self.S[root2] < self.S[root1] ):
        self.S[root2] += self.S[root1]
        self.S[root1] = root2
    else:
        self.S[root1]+= self.S[root2]
        self.S[root2] = root1
