'''
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. 
Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
'''

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        word_array = s.split(' ')
        mapping = {}

        # Check if pattern length matches the number of words in the sentence
        if len(word_array) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] in mapping:
                if word_array[i] != mapping[pattern[i]]:
                    return False
            else:
                if word_array[i] in mapping.values():
                    return False
                mapping[pattern[i]] = word_array[i]

        return True
        