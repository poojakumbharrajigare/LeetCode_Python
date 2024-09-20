'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        s = s.strip() 
        index = len(s) - 1
        
        while index >= 0 and s[index] != ' ':
            length += 1
            index -= 1
        
        return length