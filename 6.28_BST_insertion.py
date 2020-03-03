# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 02:42:54 2019

@author: laksh
"""

def insertNode(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left == None:
                root.left = node
            else:
                insertNode(root.left, node)
        else:
            if root.right == None:
                root.right = node
            else:
                insertNode(root.right, node)
'''
Note: In the above code, after inserting an element in subtrees, the tree is returned lo its parent. As a result, the
complete tree will get updated.
Time Complexity:O(n). Space Complcxity:O(n), for recursive stack. For iterative version, space complexity is O(1).
'''