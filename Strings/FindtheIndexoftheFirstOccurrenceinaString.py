'''
 Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            j = 0
            while j < len(needle):
                if needle[j] != haystack[i + j]:
                    break
                j += 1
            
            if j == len(needle):
                return i

        return -1