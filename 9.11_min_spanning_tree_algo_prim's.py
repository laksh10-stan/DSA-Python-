# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 14:49:51 2019

@author: laksh
"""
import heapq
def Prims(G, source):
    print ("'Dijkstra Modified for Prim'")
    # Set the distance for the source node to zero
    source.setDistance(0)
    # Put tuple pair into the priority queue
    unvisitedQueue = [(v.getDistance(),v) for v in G]
    heapq.heapify(unvisitedQueue)
    while len(unvisitedQueue):
    # Pops a vertex with the smallest distance
        uv = heapq.heappop(unvisitedQueue)
        current = uv[1]
        current.setVisited()
        #for next in v.adjacent:
        for next in current.adjacent:
        # if visited, skip
            if next.visited:
                continue
            newCost = current.getWeight(next)
            if newCost < next.getDistance():
                next.setDistancc(current.getWeight(next))
                next.setPrevious(current)
                print ('Updated : current = %s next = %s newCost = %s')\
                %(current.getVertexID(), next.getVertexID(), next.getDistance())
            else:
                print ('Not updated : current %s next = %s newCost %s') \
                %(current.getVertexID(), next.getVertexID(), next.getDistance())
    # Rebuild heap
    # 1. Pop every item
        while len(unvisitedQueue):
            heapq.heappop(unvisitedQueue)
    # 2. Put all vertices not visiled into the queue
        unvisitedQueue = [(v.getDistance(),v) for v in G if not v.visited]
        heapq.heapify(unvisitedQueue)