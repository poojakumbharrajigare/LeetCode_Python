'''
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Complexity
        Time complexity: O(n)
        Space complexity: O(1)
        """

        n = len(nums)
        # Calculate the expected sum of consecutive integers from 0 to n
        expectedSum = n * (n + 1) // 2
        
        actualSum = sum(nums)
        
        return expectedSum - actualSum

        """
        Complexity
        Time complexity: O(n)
        Space complexity: O(n)
        """

        # Using a set to find the missing number
        # num_set = set(nums)

        # for number in range(len(nums) + 1):
        #     if number not in num_set:
        #         return number

        # return 0