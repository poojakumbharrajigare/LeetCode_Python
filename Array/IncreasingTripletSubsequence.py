'''
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such 
that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
'''

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')

        for i in range(len(nums)):
            if nums[i] <= first:
                first = nums[i]
            elif nums[i] <= second:
                second = nums[i]
            else:
                return True
        
        return False