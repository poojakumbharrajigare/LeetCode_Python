'''
Given a string s, return the longest palindromic substring in s.
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLength = 0
        maxLengthStr = ""
        
        if len(s) == 1:
            return s

        for i in range(len(s)):
            L, R = i, i
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if R - L + 1 > maxLength:
                    maxLength = R - L + 1
                    maxLengthStr = s[L:R+1]
                L -= 1
                R += 1

            L, R = i, i + 1
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if R - L + 1 > maxLength:
                    maxLength = R - L + 1
                    maxLengthStr = s[L:R+1]
                L -= 1
                R += 1

        return maxLengthStr
