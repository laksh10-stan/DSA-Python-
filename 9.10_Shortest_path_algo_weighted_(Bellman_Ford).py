# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 12:15:02 2019

@author: laksh
"""

import sys
def BellmanFord(G, source):
    destination = {}
    predecessor = {}
    for node in G:
        destination[node] = sys.maxsize # We start admiting tha t the rest of nodes a rc very very far
        predecessor[node] = None
    destination[source] = 0 # For the source we know how to reach
    for i in range(len(G)- 1):
        for u in G:
            for v in G[u]: #For each neighbour of u
                # If the distance between Lhe node and lhe neighbour is lower than the one I have now
                if destination[v] > destination[u] + G[u][v]:
                    # Record this lower distance
                    destination[v] = destination[u] +  G[u][v]
                    predecessor[v] = u
    # Step 3: check for negative-weight cycles
    for u in G:
        for v in G[u]:
            assert destination[v] <= destination[u] + G[u][v]
    return destination, predecessor
if __name__ == '__main__ ':
    G = {
            'A': {'B': - 1, 'C': 4},
            'B': {'C': 3, 'D': 2, 'E': 2},
            'C': {},
            'D': {'B': 1 , 'C': 5},
            'E': {'D':-3}
        }
    print (BellmanFord(G, 'A'))