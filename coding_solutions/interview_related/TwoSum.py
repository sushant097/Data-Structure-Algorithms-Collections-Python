class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {}
        for i in range(len(nums)):
            curnum = nums[i]
            diff = target - curnum
            if diff not in record:
                record[curnum] = i
            elif diff in record:
                return [record[diff], i]

        return []