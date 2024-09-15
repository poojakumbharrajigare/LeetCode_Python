'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        left = 0
        right = len(s) - 1
        sArray = list(s)  # Convert string to a list of characters for mutability

        while left < right:
            if sArray[left] not in vowels:
                left += 1

            if sArray[right] not in vowels:
                right -= 1

            if sArray[left] in vowels and sArray[right] in vowels:
                temp = sArray[left]
                sArray[left] = sArray[right]
                sArray[right] = temp
                left += 1
                right -= 1

        return ''.join(sArray)