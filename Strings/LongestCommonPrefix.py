'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        if len(strs) == 1:
            return strs[0]

        min_length = len(strs[0])
        for i in range(1, len(strs)):
            if min_length > len(strs[i]):
                min_length = len(strs[i])

        prefixIndex = 0
        result = ""
        while prefixIndex < min_length:
            for i in range(1, len(strs)):
                if strs[0][prefixIndex] != strs[i][prefixIndex]:
                    return result

            result += strs[0][prefixIndex]
            prefixIndex += 1

        return result