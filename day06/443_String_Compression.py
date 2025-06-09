class Solution:
    def compress(self,chars: List[str]) -> int:
        n = len(chars)
        idx = 0
        i = 0
        
        while i < n:
            ch = chars[i]
            count = 0
            
            while i < n and chars[i] == ch:
                count = count + 1
                i = i + 1
            
            chars[idx] = ch
            idx = idx + 1
            
            if count > 1:
                for digit in str(count):
                    chars[idx] = digit
                    idx = idx  + 1
                    
        return idx