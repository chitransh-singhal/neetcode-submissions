class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] != s[j]:
                skipLeft = s[i + 1 : j + 1]
                skipRight = s[i : j]
                return skipLeft == skipLeft[::-1] or skipRight == skipRight[::-1]
            i, j = i + 1, j - 1

        return True