class Solution:
    def addMinimum(self, word: str) -> int:
        i = 0
        count = 0

        while i < len(word):
            if word[i:i+3] == "abc":
                i = i + 3
            elif word[i:i+2] in ["ab", "bc", "ac"]:
                count = count + 1
                i = i + 2
            else:
                count = count + 2
                i = i + 1
        return count