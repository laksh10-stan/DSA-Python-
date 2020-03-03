# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 17:34:51 2019

@author: laksh
"""

import heapq
def dijkstra(G, source):
    print("Dijkstra's shortest path")
    # Set the distance for the source node to zero
    source.setDistance(0)
    #Put tuple pair into the priority queue
    unvisitedQueue = [(v.getDistance(),v) for v in G]
    heapq.heapify(unvisitedQueue)
    while len(unvisitedQueue):
        #Pops a vertex with the smallest dilita.nce
        uv = heapq.heappop(unvisitedQueue)
        current = uv[1]
        current.setVisited()
        #for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            newDist = current.getDistance() + current.getWeight(next)
            if newDist < next.getDistance():
                next.setDistance(newDist)
                next.setPrevious(current)
                print('Updated : current = %s next= %s newDist = %s') \
                      %(current.getVertexID(), next.getVertexID(), next.getDistance())
            else:
                print('Not updated : current = %s next = %s newDist = %s') \
                %(current.getVertexID(), next.getVertexID(), next.getDistance())
            #Rebuild heap
            # 1. Pop every item
            while len(unvisitedQueue):
                heapq.heappop(unvisitedQueue)
            # 2. Put all vertices not visited into the queue
            unvisitedQueue = [(v.getDistance(),v) for v in G if not v.visited]
            heapq.heapify(unvisitedQueue)