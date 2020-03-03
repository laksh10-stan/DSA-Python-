# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 15:52:41 2019

@author: Lakshmendra Singh
"""

import Queue
def levelOrder(root, result):
    if root is None:
        return
    q = Queue.Queue()
    q.put(root)
    node = None
    while not q.empty():
        node = q.get()
        result.append(node.getData())
        if node.getLeft()is not None:
            q.put(node.getLeft())
        if node.getRight() is not None:
            q.put(node.getRight())
'''
Time Complexity: O(n). Space Complexity: O(n). Since, in the worst case, all the nodes on the entire last level
could be in the queue simultaneously.
'''