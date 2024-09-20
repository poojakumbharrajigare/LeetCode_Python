'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
'''

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        sum = nums[0]
        result[0] = sum

        for index in range(1, len(nums)):
            sum += nums[index]
            result[index] = sum

        return result