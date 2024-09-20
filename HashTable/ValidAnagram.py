'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapping = {}

        for c in s:
            if c in mapping:
                mapping[c] += 1
            else:
                mapping[c] = 1

        for c in t:
            if c in mapping:
                mapping[c] -= 1
            else:
                return False

            if mapping[c] == 0:
                del mapping[c]

        return True