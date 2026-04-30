class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for n in nums:
            s.add(n)
        if len(s) == len(nums): return False
        else: return True