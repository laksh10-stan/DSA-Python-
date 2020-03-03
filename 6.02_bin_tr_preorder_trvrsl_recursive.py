# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 15:36:44 2019

@author: Lakshmendra Singh
"""

# Pre-order recursive traversal. The nodes' values are appended to the result list in traversal order
def preorderRecursive(root, result):
    if not root:
        return
    result.append(root.data)
    preorderRecursive(root.left, result)
    preorderRecursive(root.right, result)
'''
Time Complexity: O(n). Space Complexity: O(n).
'''