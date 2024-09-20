'''
A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr. 
If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.
'''

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        map = {}

        for string in arr:
            if string not in map:
                map[string] = 0
            map[string] += 1

        for key, value in map.items():
            if value == 1:
                k -= 1
                if k == 0:
                    return key

        return ""