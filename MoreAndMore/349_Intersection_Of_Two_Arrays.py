class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_unique = {}
        num2_unique = {}
        answer = []

        for i in range(len(nums1)):
            if nums1[i] not in num1_unique:
                num1_unique[nums1[i]] = 1
            else:
                num1_unique[nums1[i]] = num1_unique[nums1[i]] + 1
        
        for j in range(len(nums2)):
            if nums2[j] not in num2_unique:
                num2_unique[nums2[j]] = 1
            else:
                num2_unique[nums2[j]] += 1
        
        for key in num1_unique.keys():
            if key in num2_unique.keys() and key not in answer:
                answer.append(key)
        
        return answer

        # Alternate easy solution
        # set1 = set(nums1)
        # set2 = set(nums2)

        # return list(set1 & set2)
        