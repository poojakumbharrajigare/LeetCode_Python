'''
 Given an integer array nums, return the third distinct maximum number in this array. 
 If the third maximum does not exist, return the maximum number.
'''

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        firstMax, secondMax, thirdMax = None, None, None

        for item in nums:
            if item == firstMax or item == secondMax or item == thirdMax:
                continue

            if firstMax is None or item > firstMax:
                thirdMax = secondMax
                secondMax = firstMax
                firstMax = item
            elif secondMax is None or item > secondMax:
                thirdMax = secondMax
                secondMax = item
            elif thirdMax is None or item > thirdMax:
                thirdMax = item

        return thirdMax if thirdMax is not None else firstMax