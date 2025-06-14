class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        freq = {}

        for num in nums:
            complement = k - num

            if complement in freq and freq[complement] > 0:
                count = count + 1
                freq[complement] = freq[complement] - 1
            else:
                if num in freq:
                    freq[num] = freq[num] + 1
                else:
                    freq[num] = 1
            
        return count
       