"""
Date        : 10 Febuary 2022
Runtime     : 32 ms, faster than 68.61% of Python3 online submissions for Reverse Integer.
Memory Usage: 14 MB, less than 91.00% of Python3 online submissions for Reverse Integer.
"""

import math

class Solution:
    def reverse(self, x: int) -> int:
        
        INT_MAX_VALUE = (2**31)-1 # 2147483647
        INT_MIN_VALUE = -2**31    #-2147483648
        
        num, revNum = x, 0
        
        while(num != 0):
            # pop operation
            pop = int(math.fmod(num, 10))
            num = int(num / 10)
            
            # check will it cause overflow before push
            if revNum > int(INT_MAX_VALUE / 10) or (revNum == int(INT_MAX_VALUE / 10) and pop > int(math.fmod(INT_MAX_VALUE, 10))):
                return 0
        
            if revNum < int(INT_MIN_VALUE / 10) or (revNum == int(INT_MIN_VALUE / 10) and pop < int(math.fmod(INT_MIN_VALUE, 10))):
                return 0
        
            # push operation
            revNum = (revNum * 10) + pop
            
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
        self.assertEqual(func(7463847412), 2147483647)
        self.assertEqual(func(8463847412), 0)
        self.assertEqual(func(-8463847412), -2147483648)
        self.assertEqual(func(-9463847412), 0)

if __name__ == '__main__':
    unittest.main()