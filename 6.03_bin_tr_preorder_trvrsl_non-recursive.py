# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 16:09:04 2019

@author: Lakshmendra Singh
"""

#Pre-order iterative traversal. The nodes' values are appended to the result list in traversal order
def preorder_iterative(root, result):
    if not root:
        return
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        result.append(node.data)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
'''
Time Complexity: O(n). Space Complexity: O(n).
'''