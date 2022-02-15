"""
Date        : 15 Febuary 2022
Runtime     : 36 ms, faster than 60.67% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 14 MB, less than 80.09% of Python3 online submissions for Letter Combinations of a Phone Number.
"""

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = { "2": "abc",
                        "3": "def",
                        "4": "ghi",
                        "5": "jkl",
                        "6": "mno",
                        "7": "qprs",
                        "8": "tuv",
                        "9": "wxyz" }
        
        def backtrack(i, curStr):
            
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)
        
        if digits:
            backtrack(0, "")
        
        return res

import unittest

class letterCombinationsCase(unittest.TestCase):
    def test_letterCombinations(self):
        func = Solution().letterCombinations
        self.assertEqual(func("23"), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
        self.assertEqual(func(""), [])
        self.assertEqual(func("2"), ["a", "b", "c"])

if __name__ == '__main__':
    unittest.main()
    