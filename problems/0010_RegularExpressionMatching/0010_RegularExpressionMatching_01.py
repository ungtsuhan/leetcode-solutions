"""
Date        : 11 Febuary 2022
Runtime     : 75 ms, faster than 50.24% of Python3 online submissions for Regular Expression Matching.
Memory Usage: 14.7 MB, less than 11.91% of Python3 online submissions for Regular Expression Matching.
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        cache = {}
        
        def dfs(i, j):

            if (i, j) in cache:
                return cache[(i,j)]
            
            if i >= len(s) and j >= len(p):
                return True
            
            if j >= len(p):
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if (j + 1) < len(p) and p[j + 1] == "*":
                cache[(i,j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
                return cache[(i,j)]
            if match:
                cache[(i,j)] = dfs(i + 1, j + 1)
                return cache[(i,j)]
            
            cache[(i,j)] = False
            return False
    
        return dfs(0, 0)

import unittest

class isMatchCase(unittest.TestCase):
    def test_isMatch(self):
        func = Solution().isMatch
        self.assertEqual(func("aa", "a"), False)
        self.assertEqual(func("aa", "a*"), True)
        self.assertEqual(func("ab", ".*"), True)

if  __name__ == '__main__':
    unittest.main()