class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums = sorted(nums)
        dict = {}
        result = []
        for i in range(len(sortedNums)):
            if sortedNums[i] not in dict:
                dict [sortedNums[i]] = i
        for i in nums:
            result.append(dict[i])
        return result