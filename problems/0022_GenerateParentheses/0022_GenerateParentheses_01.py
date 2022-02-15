"""
Date        : 15 Febuary 2022
Runtime     : 71 ms, faster than 14.66% of Python3 online submissions for Generate Parentheses.
Memory Usage: 14.3 MB, less than 71.94% of Python3 online submissions for Generate Parentheses.
"""

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open parenthesis if open < n
        # only add a closing parenthesis if close < open
        # valid if open == close == n
        
        stack = []
        res = []
        
        def backtrack(openN: int, closeN: int):
            
            if openN == closeN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()
            
            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()
                
        backtrack(0,0)
        return res

import unittest

class generateParenthesisCase(unittest.TestCase):
    def test_generateParenthesis(self):
        func = Solution().generateParenthesis
        self.assertEqual(func(3), ["((()))", "(()())", "(())()", "()(())", "()()()"])
        self.assertEqual(func(1), ["()"])

if __name__ == '__main__':
    unittest.main()