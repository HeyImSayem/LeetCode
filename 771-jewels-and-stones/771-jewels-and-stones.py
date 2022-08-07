class Solution:
    
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        jewel = set(J)
        return sum( 1 for item in S if item in jewel )