class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        i = 0
        j = 0
        while j < len(arr):
            if arr[j] == 0:
                i = j
                j += 1
                arr.insert(i, 0)
                arr.pop()
            j += 1
                
        