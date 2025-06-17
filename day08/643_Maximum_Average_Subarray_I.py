class Solution:
    def findMaxAverage(Self, nums: List[int], k:int) -> float:
        
        currSum = 0
        maxSum = 0
        
        for i in range(0,k):
            currSum = currSum + nums[i]
            maxSum = currSum
            
        for i in range(k,len(nums)):
            currSum = currSum + nums[i] - nums[i-k]
            
            if maxSum < currSum:
                maxSum = currSum
        
        return maxSum / k