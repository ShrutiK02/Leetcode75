class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        n = len(s)
        i = 0
        

        while i < n//2:
            s[i] , s[n - 1 - i] = s[n - 1 - i], s[i]
            i = i + 1
        return " ".join(s)
