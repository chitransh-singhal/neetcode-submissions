class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        prefix = [0] * l
        suffix = [0] * l
        ans = [0] * l
        prefix[0] = suffix[l-1] = 1
        for i in range(1,l):
            prefix[i] = nums[i-1] * prefix[i-1]
        
        for i in range(l-2, -1, -1):
            suffix[i] = nums[i+1] * suffix[i+1]
        
        for i in range(l):
            ans[i] = prefix[i] * suffix[i]
        
        return ans