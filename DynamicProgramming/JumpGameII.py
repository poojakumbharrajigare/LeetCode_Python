'''
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, 
if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
'''

class Solution:
    def jump(self, nums: List[int]) -> int:
        result = 0
        currentIndex = 0
        nextIndex = 0

        if len(nums) == 1:
            return 0

        for i in range(len(nums)):
            nextIndex = max(nextIndex, i + nums[i])

            if i == currentIndex:
                result += 1
                currentIndex = nextIndex
                if currentIndex >= len(nums) - 1:
                    break
        
        return result