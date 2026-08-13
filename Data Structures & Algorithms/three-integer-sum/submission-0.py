class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i,val in enumerate(nums):
            # reducing no. of iterations as all remaining numbers are positive
            if val > 0:
                break
            # for avoiding duplicate enteries
            if i > 0 and val == nums[i-1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                threeSum = val + nums[j] + nums[k]
                if threeSum > 0:
                    k -= 1
                elif threeSum < 0:
                    j += 1
                else:
                    res.append([val, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    # skip duplicate values of j
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        return res