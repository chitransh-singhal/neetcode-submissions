class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l = len(nums)
        freq = l // 3
        count = {}
        res = []
        for n in nums:
            count[n] = count.get(n, 0) + 1
            if count[n] == freq + 1:
                res.append(n)
        return res