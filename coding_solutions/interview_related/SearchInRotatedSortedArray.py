# clear explanation: https://www.youtube.com/watch?v=oTfPJKGEHcc

'''
Approach: Binary Search

Point to note: In a rotated sorted array, when doing binary search, one side will always be sorted and other side will always be incorrectly sorted if 
pivot index k (1 <= k < nums.length)


1. find mid. 
2. if left side is sorted
    - if target is within left limits, binary search on left
    - else binary search on right
3 else (if left side is not sorted, right side is sorted)
    - if target is within right limits, binary search on right
    - else binary search on left


'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = l + (r-l) // 2
            if nums[m] == target:
                return m
            
            elif nums[m] >= nums[l]: # strictly increasing
                if target <= nums[m] and target >=nums[l]:
                    # search in left part
                    r = m - 1
                else:
                    # search in right part
                    l = m + 1
            else:
                if target >= nums[m] and target <= nums[r]:
                    # search in right part
                    l = m + 1
                else:
                    # search in left part
                    r = m - 1
        
        return -1
            