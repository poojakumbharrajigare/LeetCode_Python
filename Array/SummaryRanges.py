'''
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
'''

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        startIndex = 0

        for i in range(len(nums)):
            if i != len(nums) - 1:
                if nums[i + 1] == nums[i] + 1:
                    continue

            range_str = ""
            if startIndex == i:
                range_str = str(nums[startIndex])
            else:
                range_str = str(nums[startIndex]) + "->" + str(nums[i])

            result.append(range_str)
            startIndex = i + 1

        return result