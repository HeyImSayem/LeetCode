class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        
        for i in range(2, len(s)):
            if len(set(s[i-2:i+1])) == 3:
                count += 1
        return count