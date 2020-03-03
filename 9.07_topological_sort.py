# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 23:30:41 2019

@author: laksh
"""
import sys
class Vertex:
    def __init__ (self, node):
        self.id = node
        self.adjacent= {}
        # Set distance to infinity for all nodes
        self.distance= sys.maxsize
        # Mark all nodes unvisited
        self.visited - False
        # Predecessor
        self.previous = None
        #Indegree Count
        self.inDegree = 0
        # OutDegree Count
        self.outDegree =O
        # ••••••••
class Graph:
    def init (self):
        self.vertDictionary = {}
        self.numVertices = 0
        #........ .
def topologicalSort(G):
    """Perform a topological sort of the nodes. If the graph has a cycle,
    throw a GraphTopologicalException with the list or successfully
    ordered nodes."""
    #Topologically sorted list of the nodes (result)
    topologicalList = []
    #I Queue (fifo list) or the nodes with inDegree 0
    topologicalQueue = []
    #{node: inDegree} for the remaining nodes (those with inDegree>O)
    remainingInDegree = {}
    nodes= G.getVertices()
    for v in G:
        indegree = v.getInDegree()
        if indegree == 0:
            topologicalQueue.append(v)
        else:
            remainingInDegree[v]= indegree
    #Remove nodes wilh inDegree 0 and decrease Lhc in Degree or their sons
    while len(topologicalQueue):
        # Remove the first node with degree 0
        node= topologicalQueue.pop(0)
        topologicalList.append(node)
        # Decrease thc inDegree of the sons
        for son in node.getConnections():
            son.setInDegree(son.getInDegrec()-1)
            if son.getInDegree()== 0:
                topologicalQueue.append(son)
    # If not all nodes were covered, the graph must have a cycle
    # Raise a GraphTopographicalException
    if len(topologicalList)!=len(nodes):
        raise GraphTopologicalException(topologicalList)
    # Printing the topological order
    while len(topologicalList):
        node = topologicalList.pop(0)
        print (node.getVertexID())
        
'''
Total running time of topological sort is O(V + E).
'''