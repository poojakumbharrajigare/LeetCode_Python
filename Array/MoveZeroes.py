'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            nonZero = i + 1
            
            if nums[i] == 0:
                while nonZero < len(nums) and nums[nonZero] == 0:
                    nonZero += 1
                
                if nonZero < len(nums):
                    self.swap(nums, i, nonZero)
    
    def swap(self, nums, number1, number2):
        temp = nums[number1]
        nums[number1] = nums[number2]
        nums[number2] = temp