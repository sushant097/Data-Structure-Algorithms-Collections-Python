'''
Maximum Depth of Binary Tree
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        else:
            # Compute the depth of each subtree
            lDepth = self.maxDepth(root.left)
            rDepth = self.maxDepth(root.right)
            
            if rDepth > lDepth: 
                return rDepth+1
            else:
                return lDepth+1
        
        