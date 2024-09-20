'''
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
'''

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map = defaultdict(int)  
        result = []

        for item in nums1:
            map[item] += 1

        for item in nums2:
            if map[item] > 0:
                result.append(item)
                map[item] -= 1

        return result