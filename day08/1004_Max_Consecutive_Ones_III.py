class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        maxLength = 0
        countZero = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                countZero += 1
            while countZero > k:
                if nums[left] == 0:
                    countZero -= 1
                left = left + 1
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength