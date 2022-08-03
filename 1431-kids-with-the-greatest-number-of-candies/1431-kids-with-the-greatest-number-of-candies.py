class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        list = []
        most_candy = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= most_candy:
                list.append(True)
            else: 
                list.append(False)
        return list