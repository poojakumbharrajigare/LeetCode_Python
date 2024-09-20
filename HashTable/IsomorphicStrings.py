'''
 Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapSToT = {}
        mapTToS = {}

        for i in range(len(s)):
            charS = s[i]
            charT = t[i]

            if charS in mapSToT:
                if mapSToT[charS] != charT:
                    return False
            else:
                mapSToT[charS] = charT

            if charT in mapTToS:
                if mapTToS[charT] != charS:
                    return False
            else:
                mapTToS[charT] = charS

        return True