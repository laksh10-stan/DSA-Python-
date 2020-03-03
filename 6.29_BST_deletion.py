# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 02:48:15 2019

@author: laksh
"""
#Note: We can replace with minimum element in right subtree also.
def deleteNode(root, data):
    '''delete the node with the given data and return the root node of the tree '''
    if root.data == data:
        # found the node we need to delete
        if root.right and root.left:
            #get the successor node and its parent
            [psucc, succ] = findMin(root.right, root)
            #splice out the successor
            # (we need the parent to do this)
            if psucc.left == succ:
                psucc.left = succ.right
            else:
                psucc.right = succ.right
            # reset the left and right children of the successor
            succ.left = root.left
            succ.right = root.right
            return succ
        else:
            # "easier" case
            if root.left:
                return root.left # promote the left subtree
            else:
                return root.right # promote the right subtree
    else:
        if root.data > data: # data should be in the left subtree
            if root.left:
                root.left = deleteNode(root.left, data)
            # else the data is not in the tree
        else: #data should be in Lhe righl subtree
            if root.right:
                root.right = deleteNode(root.right, data)
    return root
def findMin(root, parent):
    """ return the minimum node in the current tree and its parent """
    '''
    we use an ugly trick: the parent node is passed in as an argument
    so that eventually when the leftmost child is reached, the
    call can return both the parent to the successor and the successor
    '''
    if root.left:
        return findMin(root.left, root)
    else:
        return [parent, root]
'''
Time Complexity: O(n).
Space Complexity: O(n) for recursive stack. For iterative version , space complexity is O(1)
'''