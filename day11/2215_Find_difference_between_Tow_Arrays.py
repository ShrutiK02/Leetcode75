class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = []
        num1_unique = []
        num2_unique = []

        for i in range(len(nums1)):
            if nums1[i] not in nums2 and nums1[i] not in num1_unique:
                num1_unique.append(nums1[i])
        
        for k in range(len(nums2)):
            if nums2[k] not in nums1 and nums2[k] not in num2_unique:
                num2_unique.append(nums2[k])
        
        answer.append(num1_unique)
        answer.append(num2_unique)

        return answer
        