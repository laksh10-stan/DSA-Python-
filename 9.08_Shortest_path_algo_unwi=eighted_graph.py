# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 23:45:00 2019

@author: laksh
"""

class Vertex:
    def __init__ (self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance= -1
        # Mark all nodes unvisited
        self.visited = False
        # Predecessor
        self.previous = None
        # •••••••••
class Graph:
    def __init__ (self):
        self.vertDictionary = {}
        self.numVertices = 0
def UnweightedShortestPath(G,s):
    source = G.getVertex(s)
    source.setDistance(0)
    source.setPrevious(None)
    vertQueue = Queue()
    vertQueue.enQueue(source)
    while (vertQueue.size > 0):
        currentVert = vertQueue.deQueue()
        for nbr in currentVert.getConnections():
            if nbr.getDistance() == -1:
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPrevious(currentVert)
                vertQueue.enQueue(nbr)
    for v in G.vertDictionary.values():
        print (source.getVertexID(), " to ",v.getVertexID(), "-->",v.getDistance())
'''
T(c): O(|E|+|V|) if adjacency lists are used

T(c): O(|V|^2) if adjacency matrix are used
