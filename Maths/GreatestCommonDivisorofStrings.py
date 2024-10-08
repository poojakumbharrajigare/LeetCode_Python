'''
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t 
(i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
'''

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ""
    
        gcd_len = gcd(len(str1), len(str2))
    
        return str1[:gcd_len]

def gcd(n1, n2):
    while n1 != 0 and n2 != 0:
        if n1 > n2:
            n1 %= n2
        else:
            n2 %= n1
    
    return n1 or n2  # Return n1 if it's not zero, otherwise return n2