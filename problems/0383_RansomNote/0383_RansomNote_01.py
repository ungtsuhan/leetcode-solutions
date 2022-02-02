"""
Date        : 2 Febuary 2022
Runtime     : 52 ms, faster than 81.29% of Python3 online submissions for Ransom Note.
Memory Usage: 14.1 MB, less than 99.21% of Python3 online submissions for Ransom Note.
"""

import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        queueLength = len(ransomNote)
        charCount = collections.Counter(ransomNote)

        for i in magazine:
            if i in charCount and charCount[i] > 0:
                queueLength -= 1
                charCount[i] -= 1
                if queueLength == 0:
                    return True
        return False

import unittest

class canConstructCase(unittest.TestCase):
    def test_canConstruct(self):
        func = Solution().canConstruct
        self.assertEqual(func("a", "b"), False)
        self.assertEqual(func("aa", "ab"), False)
        self.assertEqual(func("aa", "aab"), True)

if __name__ == "__main__":
    unittest.main()