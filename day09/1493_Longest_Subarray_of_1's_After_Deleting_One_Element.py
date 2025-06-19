class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        max_len = 0
        zeroCount = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroCount += 1
            
        while zeroCount > 1:
            if nums[left] == 0:
                zeroCount -= 1
            left += 1
        
        window_size = right - left
        max_len = max(max_len, window_size)
        
        return max_len