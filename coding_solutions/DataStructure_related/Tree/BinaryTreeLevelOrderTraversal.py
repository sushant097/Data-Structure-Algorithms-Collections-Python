'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level)

Example:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Recursive Solution
        # Time: O(n); Space: O(n)
        result = []
        if root is None:
            return result
        
        def traverse(node, level):
            if node is None:
                return
            if len(result) == level:
                result.append([])
            
            result[level].append(node.val)
            
            traverse(node.left, level+1)
            traverse(node.right, level+1)
        
        traverse(root, 0)
        return result
    
            
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Iterative Solution
        # Time: O(n); Space: O(n)
        result = [] # final result
        if root is None: return result
        queue = []  # for level order traversal
        queue.append(root)
        while(len(queue) > 0):
            size = len(queue)
            currLevel = []
            while(size > 0):
                size -= 1
                curr = queue.pop(0)
                currLevel.append(curr.val)
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
            result.append(currLevel)
        return result
       