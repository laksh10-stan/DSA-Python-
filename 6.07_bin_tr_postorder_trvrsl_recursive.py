# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 15:52:19 2019

@author: Lakshmendra Singh
"""

# Post-order iterative traversal. The nodes' values are appended to the result list in traversal order
def postorderIterative(root, result):
    if not root:
        return
    visited = set()
    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if node.right and not node.right in visited:
                stack.append(node)
                node = node.right
            else:
                visited.add(node)
                result.append(node.data)
                node = None
'''
Time Complexity: O(n). Space Complexity: O(n).
'''