'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
'''
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()  # Using a set to track seen numbers
        new_number = 0
        
        while n != 1:
            new_number = 0
            
            # Calculate the sum of squares of digits
            while n > 0:
                digit = n % 10
                n //= 10  # Integer division to remove the last digit
                new_number += digit * digit

            # If the number has already been seen, it's a cycle, so return False
            if new_number in seen:
                return False

            # Add the new number to the set
            seen.add(new_number)
            n = new_number
        
        return True