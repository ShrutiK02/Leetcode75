class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
            max = 0
            for candy in candies:
                if candy >= max:
                    max = candy
                
            result = []
            for i in range(len(candies)):
                if candies[i] + extraCandies >= max:
                    result.append(True)
                else:
                    result.append(False)
            
            return result
            
        #return [x+extraCandies >= max(candies) for x in candies]
