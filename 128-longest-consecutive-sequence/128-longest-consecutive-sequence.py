class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count,mx_count = 1,1
        if nums==[]:
            return 0
        
        nums = list(set(nums))
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]==1:
                count+=1
            else:
                count=1
            
            mx_count=max(count,mx_count)
        return mx_count