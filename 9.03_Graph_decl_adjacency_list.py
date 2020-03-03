# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 17:06:55 2019

@author: laksh
"""
import sys
class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = 0
        # Set distance to infinity for aJI nodes
        self.distance = sys.maxsize
        # Mark all nodes unvisited
        self.visited = False
        # Predecessor
        self.previous = None
class Graph:
    def __init__(self):
        self.vertDictionary = {}
        self.numVertices = 0