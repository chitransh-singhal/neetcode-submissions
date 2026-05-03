class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        countArr = [0] * 3
        for n in nums:
            countArr[n] += 1
        idx = 0
        for i in range(3):
            while countArr[i]:
                countArr[i] -= 1
                nums[idx] = i
                idx += 1