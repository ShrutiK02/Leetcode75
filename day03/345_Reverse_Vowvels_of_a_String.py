class Solution:
    
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        # volwels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        volwels = set('aeiouAEIOU')
        s = list(s)

        def swap(s, v1, v2):
            # s = [i for i in s]
            a = s[v1]
            s[v1] = s[v2]
            s[v2] = a
            return s

        while left < right:
            if s[left] not in volwels:
                left = left + 1
            else:
                if s[right] not in volwels:
                    right = right - 1
                else:
                    s = swap(s, right, left)
                    left = left + 1
                    right = right - 1
        return "".join(s)

    

