'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        isPalindrome = True

        alphaNumericString = []

        for c in s:
            if c.isalnum():
                alphaNumericString.append(c.lower())

        for i in range(len(alphaNumericString) // 2):
            if alphaNumericString[i] != alphaNumericString[len(alphaNumericString) - i - 1]:
                isPalindrome = False
                break

        return isPalindrome