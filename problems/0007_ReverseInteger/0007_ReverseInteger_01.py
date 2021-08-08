"""
Date        : 8 August 2021
Runtime     : 32 ms, faster than 68.61% of Python3 online submissions for Reverse Integer.
Memory Usage: 14 MB, less than 91.00% of Python3 online submissions for Reverse Integer.
"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        p, revNum = abs(x), 0
        isPositive = True if x >= 0 else False

        while p > 0:
            revNum = (revNum * 10) + (p % 10)
            p = p // 10
        
        if not isPositive:
            revNum = -revNum

        # return 0 if reversed value outside the signed 32-bit integer range
        if abs(revNum) > ((1 << 31) - 1):
            return 0
        
        return revNum

# Unit Test
import unittest
class ReverseCase(unittest.TestCase):
    def test_reverse(self):
        func = Solution().reverse
        self.assertEqual(func(123), 321)
        self.assertEqual(func(-123), -321)
        self.assertEqual(func(120), 21)
        self.assertEqual(func(0), 0)
        self.assertEqual(func(1534236469), 0)

if __name__ == '__main__':
    unittest.main()