class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        
        prefix = strs[0]
        prefix_len = len(strs[0])

        for s in strs[1:]:
            while prefix != s[0:prefix_len]:
                prefix_len = prefix_len - 1
                prefix = prefix[0:prefix_len]
                if prefix_len == 0:
                    return ""
        
        return prefix
            

        
        