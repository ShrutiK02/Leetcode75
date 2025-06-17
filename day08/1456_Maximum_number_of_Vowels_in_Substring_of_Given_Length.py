class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        right = 0
        maxVowel = 0
        count = 0
        
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        while right < k:
            if s[right] in vowels:
                count = count + 1
            right = right + 1
        
        maxVowel = count
        
        while right < len(s):
            if s[right] in vowels:
                count = count + 1
            if s[left] in vowels:
                count = count - 1
            maxVowel = max(maxVowel, count)
            left = left + 1
            right = right + 1
        return maxVowel
                