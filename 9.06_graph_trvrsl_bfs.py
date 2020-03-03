# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 22:59:54 2019

@author: laksh
"""

def BFSTraversal(G,s):
    start = G.getVertex(s)
    start.setDistance(0)
    start.setPrevious(None)
    vertQueue = Queue()
    vertQueue.enQueue(start)
    while (vertQueue.size > 0):
        currentVert = vertQueue.deQueue()
        print(currentVert.getVertexID())
        for nbr in currentVert.getConnections():
            if  (nbr.getColor() =='white'):
                nbr.setColor('gray')
                nbr.set.Distance(currentVert.getDistance() + 1)
                nbr.setPrevious(currentVert)
                vertQueue.enQueue(nbr)
            currentVert.setColor('black')
def BFS(G):
    for v in G:
        if (v.getColor()=='white'):
            BFSTraversal(G, v.getVertexID())