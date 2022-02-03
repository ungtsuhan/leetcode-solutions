"""
Date        : 2 Febuary 2022
Runtime     : 52 ms, faster than 71.02% of Python3 online submissions for Valid Anagram.
Memory Usage: 14.5 MB, less than 80.91% of Python3 online submissions for Valid Anagram.
"""

import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = collections.Counter(s)
        count2 = collections.Counter(t)
        return True if count1 == count2 else False

import unittest

class isAnagramCase(unittest.TestCase):
    def test_isAnagram(self):
        func = Solution().isAnagram
        self.assertEqual(func("anagram", "nagaram"), True)
        self.assertEqual(func("rat", "car"), False)

if __name__ == "__main__":
    unittest.main()