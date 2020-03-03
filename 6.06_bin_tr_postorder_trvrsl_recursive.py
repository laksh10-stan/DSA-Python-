# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 15:52:17 2019

@author: Lakshmendra Singh
"""

# Post-order recursive traversal. The nodes' values are appended to the result list in traversal order
def postorderRecursive(root, result):
    if not root:
        return
    postorderRecursive(root.left, result)
    postorderRecursive(root.right, result)
    result.append(root.data)
'''
Time Complexity: O(n). Space Complexity: O(n).
'''