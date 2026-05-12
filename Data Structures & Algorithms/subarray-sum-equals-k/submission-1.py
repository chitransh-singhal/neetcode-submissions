class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = curr = 0
        prefixSums = { 0 : 1 }

        for i in range(len(nums)):
            curr += nums[i]
            diff = curr - k
            if diff in prefixSums:
                ans += prefixSums[diff]
            if curr in prefixSums:
                prefixSums[curr] += 1
            else:
                prefixSums[curr] = 1

        return ans