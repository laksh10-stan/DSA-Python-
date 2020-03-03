# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 15:08:32 2019

@author: laksh
"""

#MAKESET
class makeSet:
    def __init__ (self, n):
        self.MAKESET(n)
    def MAKESET(self, n):
        self.S =[x for x in range(n)]
#FIND
def find(self, X):
    if( S[X] == X ):
        return X
    else:
        return find([X])
#UNION

def union(self, root1, root2):
    S[root1] = root2
def kruskal(G):
    edges = []
    for v in G:
        makeSet(v.getVertexID())
        for w in v.getConnections():
            vid = v.getVertexID()
            wid = w.getVertexID()
            edges.append((v.getWeight(w),vid, wid))
    edges.sort()
    minimumSpanningTree = set()
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
           union(vertice1, vertice2)
           minimumSpanningTree.add(edge)
        return minimumSpanningTree