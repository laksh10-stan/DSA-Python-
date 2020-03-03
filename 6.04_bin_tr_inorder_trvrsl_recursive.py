# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 15:41:16 2019

@author: Lakshmendra Singh
"""

# In-order recursive traversal. The nodes' values are appended to the result list in traversal order
def inorderRecursive(root, result):
    if not root:
        return
    inorderRecursive(root.left, result)
    result.append(root.data)
    inorderRecursive(root.right, result)
'''
Time Complexity: O(n). Space Complexity: O(n).
'''