class Solution:
 def isSubsequence(self, s: str, t: str) -> bool:
    #Initialize two pointers to 0 each for s and t
    sp = 0
    tp = 0
     
    # Keep iterating through t as it is the main string.
    # check if corresponsing elements of s and t are same if they are then increment sp
    # Increment tp at each iteration
     
    while sp < len(s) and tp < len(t):
        if s[sp] == t[tp]:
             sp = sp + 1
        tp = tp + 1
    
    # check if value of sp is same as len(s) and return the boolean
    return sp == len(s)    
    