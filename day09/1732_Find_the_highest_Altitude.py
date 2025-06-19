class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        high = 0
        sum = 0
        for i in range(len(gain)):
            sum = sum + gain[i]
            if high < sum:
                high = sum
        return high