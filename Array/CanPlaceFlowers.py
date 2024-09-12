'''
You have a long flowerbed in which some of the plots are planted, and some are not. 
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, 
return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
'''

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        previous = 0
        next_flower = 0

        for i in range(len(flowerbed)):
            if i != len(flowerbed) - 1:
                next_flower = flowerbed[i + 1]
            else:
                next_flower = 0  # This ensures next is 0 for the last element
            
            if flowerbed[i] == 0 and previous == 0 and next_flower == 0:
                n -= 1
                flowerbed[i] = 1  # Plant a flower
            
            previous = flowerbed[i]  # Update previous to current

        return n <= 0