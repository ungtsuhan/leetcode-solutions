'''
Date        : 3 March 2022
Runtime     : 36 ms, faster than 82.92% of Python3 online submissions for Divide Two Integers.
Memory Usage: 13.9 MB, less than 90.21% of Python3 online submissions for Divide Two Integers.
'''

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        isPositive = True if ((dividend >= 0) == (divisor >= 0)) else False
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0
        
        while dividend - divisor >= 0:
            count = 0
            while dividend - (divisor << 1 << count) >= 0:
                count += 1
            result += 1 << count
            dividend -= divisor << count
        
        if not isPositive:
            result = -result
            
        return min(max(-2147483648, result), 2147483647)

import unittest
class divideCase(unittest.TestCase):
    def test_divide(self):
        func = Solution().divide
        self.assertEqual(func(10, 3), 3)
        self.assertEqual(func(7, -3), -2)

if __name__ == '__main__':
    unittest.main()