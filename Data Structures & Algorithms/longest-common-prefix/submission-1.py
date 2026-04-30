class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        str1 = strs[0]
        str2 = strs[-1]
        res = ""
        for i in range(min(len(str1), len(str2))):
            if str1[i] == str2[i]:
                res += str1[i]
            else: break
        
        return res