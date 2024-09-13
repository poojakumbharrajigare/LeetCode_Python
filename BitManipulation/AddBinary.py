'''
Given two binary strings a and b, return their sum as a binary string.
'''

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        carry = 0
        a_index = len(a) - 1
        b_index = len(b) - 1

        while a_index >= 0 or b_index >= 0 or carry > 0:
            number1 = int(a[a_index]) if a_index >= 0 else 0
            number2 = int(b[b_index]) if b_index >= 0 else 0

            # Calculate the sum of the current digits and the carry
            sum_val = number1 + number2 + carry
            result.append(str(sum_val % 2))  # Append the remainder (binary digit)

            carry = sum_val // 2  # Update the carry

            # Move to the next digits
            a_index -= 1
            b_index -= 1

        return ''.join(result[::-1])  # Reverse and join the result list to form the final string