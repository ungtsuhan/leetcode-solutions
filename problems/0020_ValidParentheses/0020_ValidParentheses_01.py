"""
Date        : 5 Febuary 2022
Runtime     : 24 ms, faster than 97.85% of Python3 online submissions for Valid Parentheses.
Memory Usage: 13.8 MB, less than 96.63% of Python3 online submissions for Valid Parentheses.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        parenthesesMap = {'(' : ')', '{' : '}', '[' : ']' }
        stack = []
        for i, v in enumerate(s):
            if v in parenthesesMap:
                stack.append(parenthesesMap[v])
            else:
                if not stack:
                    return False

                if stack.pop() != v:
                    return False
                
        return True if not stack else False

import unittest

class isValidCase(unittest.TestCase):
    def test_isValidCase(self):
        func = Solution().isValid
        self.assertEqual(func("()"), True)
        self.assertEqual(func("()[]{}"), True)
        self.assertEqual(func("(]"), False)

if __name__ == "__main__":
    unittest.main()