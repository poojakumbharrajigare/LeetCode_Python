'''
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
'''

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []

        while columnNumber > 0:
            result.insert(0, chr(((columnNumber - 1) % 26) + ord('A')))
            columnNumber = (columnNumber - 1) // 26

        return ''.join(result)