class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            if height[left] < height[right]:
                area_cal = height[left] * width
            else:
                area_cal = height[right] * width

            if maxarea < area_cal:
                maxarea = area_cal
            
            if height[left] <= height[right]:
                left = left + 1
            else:
                right = right - 1

        return maxarea
