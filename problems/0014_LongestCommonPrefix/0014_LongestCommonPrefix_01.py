"""
Date        : 11 Febuary 2022
Runtime     : 46 ms, faster than 49.54% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 14 MB, less than 78.82% of Python3 online submissions for Longest Common Prefix.
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        result = ""
        
        while True:
            char = ""
            
            for j in range(len(strs)):    
                # return if index no more character
                if i >= len(strs[j]):
                    return result
                
                # record char for first item
                if j == 0:
                    char = strs[j][i]
                
                # compare char with the char of first item
                elif strs[j][i] != char:
                    return result
            
            # if all item have the same character, append to result
            result += char
            
            # continue check for next index
            i += 1

import unittest

class longestCommonPrefixCase(unittest.TestCase):
    def test_longestCommonPrefix(self):
        func = Solution().longestCommonPrefix
        self.assertEqual(func(["flower","flow","flight"]), "fl")
        self.assertEqual(func(["dog","racecar","car"]), "")

if __name__ == "__main__":
    unittest.main()