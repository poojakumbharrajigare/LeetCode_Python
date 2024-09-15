'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        # Handle when n is equal to the smallest 32-bit integer value
        if n == -2**31:
            n = -(n + 1)
            x = 1.0 / x
            return x * x * self.myPow(x * x, n // 2)

        # If n is negative, invert x and make n positive
        if n < 0:
            x = 1.0 / x
            n = -n

        if n % 2 == 0:
            result = self.myPow(x, n // 2)
            return result * result
        else:
            result = self.myPow(x, (n - 1) // 2)
            return result * result * x