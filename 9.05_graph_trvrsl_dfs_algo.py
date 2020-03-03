# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 22:19:08 2019

@author: laksh
"""

def dfs (G, currentVert, visited):
    visited[currentVert]=True                             # Mark the visited node
    print ("traversal: " + currentVert.getVertexID())
    for nbr in currentVert.getConnections():              # Take a neighbouring node
        if nbr not in visited:                            #Check whether the neighbour node is aln::ady visited
            dfs (G, nbr, visited)                         # Recursively traverse the neighbouring node
def DFSTraversal(G):
    visited = {}                                          # Dictionary to mark the visited nodes
    for currentVert in G:                                 # G contains vertex objects
        if currentVert not in visited:                    # Start traversing from the root node only if its not visited
            dfs(G, currentVert, visited)                  #For a connected graph thls is called only once







