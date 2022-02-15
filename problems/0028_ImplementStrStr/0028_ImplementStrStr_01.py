'''
Date        : 15 Febuary 2022
Runtime     : 134 ms, faster than 34.27% of Python3 online submissions for Implement strStr().
Memory Usage: 14.2 MB, less than 71.95% of Python3 online submissions for Implement strStr().
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        
        for i in range(len(haystack) + 1 - len(needle)):
            if haystack[i: i+len(needle)] == needle:
                return i
        return -1

import unittest

class strStrCase(unittest.TestCase):
    def test_strStr(self):
        func = Solution().strStr
        self.assertEqual(func("hello", "ll"), 2)
        self.assertEqual(func("aaaaa", "bba"), -1)

if __name__ == '__main__':
    unittest.main()