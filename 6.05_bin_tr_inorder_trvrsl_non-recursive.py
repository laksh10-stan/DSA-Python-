# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 15:41:18 2019

@author: Lakshmendra Singh
"""

# In-order iterative traversal. The nodes' values are appended to the result list in traversal order
def inorderIterative(root, result):
    if not root:
        return
    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            result.append(node.data)
            node = node.right
'''
Time Complexity: O(n). Space Complexity: O(n).
'''