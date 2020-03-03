# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 22:46:50 2019

@author: laksh
"""
'''
Adjacency Matrix
Graph Declaration for Adjacency Matrix
'''
class Vertex:
    def __init__(self, node):
        self.id = node
        # Mark all nodes unvisited
        self.visited = False
    def addNeighbor(self, neighbor, G):
        G.addEdge(self.id, neighbor)
    def getConnections(self, G):
        return G.adjMatrix[self.id]
    def getVertexID(self):
        return self.id
    def setVertexID(self, id):
        self.id= id
    def setVisited(self):
        self.visited =True
    def __str__(self):
        return str(self.id)
class Graph:
    def __init__ (self, numVertices, cost= 0):
        self.adjMatrix = [[-1]*numVertices for _ in range(numVertices)]
        self.numVertices =numVertices
        self.vertices = []
        for i in range(0,numVertices):
            newVertex = Vertex(i)
            self.vertices.append(newVertex)
