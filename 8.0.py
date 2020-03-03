# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 22:38:36 2019

@author: laksh
"""

#MAKESET
class DisjointSet:
    def init (self, n):
        self.MAKESET(n)
    def MAKESET(self, n):
        self.S =[x for x in range(n)]
#FIND
def FIND(self, X):
    if( S[X] == X ):
        return X
    else:
        return FIND([X])
#UNION

def UNION(self, root1, root2):
    S[root1] = root2