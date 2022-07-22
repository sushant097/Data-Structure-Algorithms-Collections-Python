'''
  Convert Sorted Array to Binary Search Tree

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

'''





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        # find middle index
        mid = len(nums) // 2
        # make the middle element of root
        root = TreeNode(nums[mid])
        
        # left subtree of root has all
        # values <arr[mid]
        root.left = self.sortedArrayToBST(nums[:mid])
        
        # right subtree of root has all
        # values > arr[mid]
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
