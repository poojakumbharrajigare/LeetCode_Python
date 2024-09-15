'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        word1Index = 0
        word2Index = 0

        while word1Index < len(word1) or word2Index < len(word2):
            first = word1[word1Index] if word1Index < len(word1) else ""
            second = word2[word2Index] if word2Index < len(word2) else ""
            if word1Index < len(word1):
                result.append(first)
                word1Index += 1
            if word2Index < len(word2):
                result.append(second)
                word2Index += 1

        return ''.join(result)