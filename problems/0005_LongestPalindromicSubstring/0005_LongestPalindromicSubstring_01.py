"""
Date        : 10 Febuary 2022
Runtime     : 1578 ms, faster than 44.65% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 13.9 MB, less than 98.55% of Python3 online submissions for Longest Palindromic Substring.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestPalindromicSubstring = ""
        
        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                currentLen = r - l + 1  
                if currentLen > len(longestPalindromicSubstring):
                    longestPalindromicSubstring = s[l:r+1]
                l -= 1
                r += 1
            
            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                currentLen = r - l + 1  
                if currentLen > len(longestPalindromicSubstring):
                    longestPalindromicSubstring = s[l:r+1]
                l -= 1
                r += 1
            
        return longestPalindromicSubstring

import unittest

class longestPalindromeCase(unittest.TestCase):
    def test_longestPalindrome(self):
        func = Solution().longestPalindrome
        self.assertEqual(func("babad"), "bab")
        self.assertEqual(func("cbbd"), "bb")

if __name__ == "__main__":
    unittest.main()