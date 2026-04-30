class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "$" + s
        
        return result

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            while  s[j] != "$":
                j+=1
            lt = int(s[i:j])
            i = j + 1
            j = i + lt
            ans.append(s[i:j])
            i = j
        
        return ans
