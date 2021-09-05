"""
Date        : 5 September 2021
Runtime     : 28 ms, faster than 81.10% of Python3 online submissions for Length of Last Word.
Memory Usage: 14.3 MB, less than 34.33% of Python3 online submissions for Length of Last Word.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.strip().split(' ')
        return len(arr[len(arr)- 1])

# Unit Test
import unittest
class LengthOfLastWordCase(unittest.TestCase):
    def test_lengthOfLastWord(self):
        func = Solution().lengthOfLastWord
        self.assertEqual(func("Hello World"), 5)
        self.assertEqual(func("   fly me   to   the moon  "), 4)
        self.assertEqual(func("luffy is still joyboy"), 6)
        
if __name__ == '__main__':
    unittest.main()