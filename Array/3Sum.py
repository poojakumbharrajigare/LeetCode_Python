'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip the same element to avoid duplicates

            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum_val = nums[i] + nums[left] + nums[right]

                if sum_val == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for `left`
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for `right`
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif sum_val < 0:
                    left += 1
                else:
                    right -= 1

        return result