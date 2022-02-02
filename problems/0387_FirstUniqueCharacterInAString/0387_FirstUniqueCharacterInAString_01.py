"""
Date        : 2 Febuary 2022
Runtime     : 97 ms, faster than 83.12% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 14.2 MB, less than 94.14% of Python3 online submissions for First Unique Character in a String.
"""

import collections

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1

import unittest

class firstUniqCharCase(unittest.TestCase):
    def test_firstUniqChar(self):
        func = Solution().firstUniqChar
        self.assertEqual(func("leetcode"), 0)
        self.assertEqual(func("loveleetcode"), 2)
        self.assertEqual(func("aabb"), -1)

if __name__ == "__main__":
    unittest.main()