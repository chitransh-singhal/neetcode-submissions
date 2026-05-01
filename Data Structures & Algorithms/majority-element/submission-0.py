class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        ans = maxC = 0
        for n in nums:
            cnt[n] += 1
            if maxC < cnt[n]:
                ans = n
                maxC = cnt[n]
        
        return ans