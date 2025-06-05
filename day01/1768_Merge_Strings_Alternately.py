class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0
        result = ""
        while i<len(word1) and j<len(word2):
            result = result + word1[i]
            result = result + word2[j]
            i = i + 1
            j = j + 1
        result = result + word1[i:] + word2[j:]
        print(result)
        return result

    #result=[]
    #While loop
    #result.append(word1[i]) etc
    #final = "".join(result)


        

        