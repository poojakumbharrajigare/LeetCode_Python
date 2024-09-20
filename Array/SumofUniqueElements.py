'''
You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.
'''

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        map = [0] * 101  
        sum = 0

        for num in nums:
            map[num] += 1

            if map[num] == 1:
                sum += num
            elif map[num] == 2:
                sum -= num

        return sum