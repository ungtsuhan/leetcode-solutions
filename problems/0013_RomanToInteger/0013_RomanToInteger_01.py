"""
Date        : 11 Febuary 2022
Runtime     : 57 ms, faster than 58.44% of Python3 online submissions for Roman to Integer.
Memory Usage: 13.9 MB, less than 84.33% of Python3 online submissions for Roman to Integer.
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}        
        result = 0
        
        for i in range(len(s)-1):
            if roman[s[i]] < roman[s[i+1]]:
                result -= roman[s[i]]
            else:
                result += roman[s[i]]
        result += roman[s[len(s)-1]]
        
        return result

import unittest

class romanToIntCase(unittest.TestCase):
    def test_romanToInt(self):
        func = Solution().romanToInt
        self.assertEqual(func("III"), 3)
        self.assertEqual(func("IV"), 4)
        self.assertEqual(func("IX"), 9)
        self.assertEqual(func("LVIII"), 58)
        self.assertEqual(func("MCMXCIV"), 1994)

if __name__ == "__main__":
    unittest.main()