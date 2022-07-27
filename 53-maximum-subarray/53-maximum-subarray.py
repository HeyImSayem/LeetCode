class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        largestSoFar = float("-inf")
        currentSum = 0
        
        for num in nums:
            currentSum += num
            
            if currentSum > largestSoFar:
                largestSoFar = currentSum
                
            if currentSum < 0:
                currentSum = 0
                
        return largestSoFar