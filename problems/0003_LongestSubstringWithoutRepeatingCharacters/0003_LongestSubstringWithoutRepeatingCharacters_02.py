"""
Date        : 10 Febuary 2022
Runtime     : 68 ms, faster than 75.74% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14 MB, less than 98.79% of Python3 online submissions for Longest Substring Without Repeating Characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l_pointer, r_pointer = 0, 0
        charCountHashSet = set()
        globalMaxLen = 0 
        
        while(r_pointer < len(s)):
            if s[r_pointer] not in charCountHashSet:
                charCountHashSet.add(s[r_pointer])
                globalMaxLen = max(globalMaxLen, len(charCountHashSet))
                r_pointer += 1
            else:
                charCountHashSet.remove(s[l_pointer])
                l_pointer += 1
        
        return globalMaxLen
                
import unittest

class lengthOfLongestSubstringCase(unittest.TestCase):
    def test_lengthOfLongestSubstring(self):
        func = Solution().lengthOfLongestSubstring
        self.assertEqual(func("abcabcbb"), 3)
        self.assertEqual(func("bbbbb"), 1)
        self.assertEqual(func("pwwkew"), 3)

if __name__ == "__main__":
    unittest.main()