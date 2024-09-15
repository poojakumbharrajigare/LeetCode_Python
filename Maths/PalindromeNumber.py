'''
Given an integer x, return true if x is a palindrome, and false otherwise.
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        number = str(x)
        result = True

        for index in range(len(number) // 2):
            if number[index] == number[len(number) - 1 - index]:
                continue
            else:
                result = False

        return result