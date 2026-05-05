class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        nums.sort()
        nums = list(dict.fromkeys(nums))
        maxC = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]+1:
                count += 1
                maxC = max(maxC, count)
            else:
                count = 1
        return maxC