class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        uniq_occurance = {}

        for i in range(len(arr)):
            if arr[i] not in uniq_occurance:
                uniq_occurance[arr[i]] = 1
            else:
                uniq_occurance[arr[i]] = uniq_occurance[arr[i]] + 1
        
        for value in uniq_occurance.values():
            if len(list(uniq_occurance.values())) != len(set(uniq_occurance.values())):
                return False
        
        return True
                
        