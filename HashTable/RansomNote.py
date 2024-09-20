'''
Given two strings ransomNote and magazine, 
return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        magazineCharCount = defaultdict(int)

        for c in magazine:
            magazineCharCount[c] += 1

        for c in ransomNote:
            if magazineCharCount[c] > 0:
                magazineCharCount[c] -= 1
            else:
                return False

        return True