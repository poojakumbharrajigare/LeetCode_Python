'''
 Given an integer array nums and an integer k, 
 return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping = {}

        for i in range(len(nums)):
            if nums[i] in mapping:
                if abs(mapping[nums[i]] - i) <= k:
                    return True
                
                mapping[nums[i]] = i
            else:
                mapping[nums[i]] = i

        return False
