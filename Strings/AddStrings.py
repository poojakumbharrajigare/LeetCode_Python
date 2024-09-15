'''
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). 
You must also not convert the inputs to integers directly.
'''

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1Index = len(num1) - 1
        num2Index = len(num2) - 1
        carry = 0
        result = []

        while num1Index > -1 or num2Index > -1 or carry != 0:
            a = int(num1[num1Index]) if num1Index > -1 else 0
            b = int(num2[num2Index]) if num2Index > -1 else 0
            num1Index -= 1
            num2Index -= 1

            total = a + b + carry
            result.insert(0, str(total % 10))
            carry = total // 10

        return ''.join(result)