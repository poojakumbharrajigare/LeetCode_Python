'''
 Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = 0
        currentSum = 0
        minLength = float('inf')  
        
        while right < n:
            currentSum += nums[right]
            right += 1

            while currentSum >= target:
                minLength = min(minLength, right - left)
                currentSum -= nums[left]
                left += 1

        return 0 if minLength == float('inf') else minLength