"""
Date        : 10 Febuary 2022
Runtime     : 41 ms, faster than 59.97% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 13.9 MB, less than 97.82% of Python3 online submissions for String to Integer (atoi).
"""

import math

class Solution:
    def myAtoi(self, s: str) -> int:
        
        INT_MAX_VALUE = (2**31)-1 # 2147483647
        INT_MIN_VALUE = -2**31    #-2147483648
        
        i = 0
        isPositive = True
        result = 0
        
        # ignore leading white space
        while i < len(s) and s[i] == " ":
            i += 1
        
        # check if next character is +/- to determine is positive or negative
        if i < len(s) and s[i] == "-":
            isPositive = False
            i += 1
        elif i < len(s) and s[i] == "+":
            isPositive = True
            i += 1
        
        checker = set("0123456789")
        while i < len(s) and s[i] in checker:
            # digit to be append
            digit = int(s[i]) if isPositive else -int(s[i])
             
            # check overflow or underflow before append
            if result > int(INT_MAX_VALUE / 10) or (result == int(INT_MAX_VALUE / 10) and digit > int(math.fmod(INT_MAX_VALUE, 10))):
                return INT_MAX_VALUE
            if result < int(INT_MIN_VALUE / 10) or (result == int(INT_MIN_VALUE / 10) and digit < int(math.fmod(INT_MIN_VALUE, 10))):
                return INT_MIN_VALUE
            
            # append the digit
            result = digit + (result * 10)
            
            # continue to check next digit
            i += 1
        
        return result

import unittest

class myAtoiCase(unittest.TestCase):
    def test_myAtoi(self):
        func = Solution().myAtoi
        self.assertEqual(func("42"), 42)
        self.assertEqual(func("   -42"), -42)
        self.assertEqual(func("4193 with words"), 4193)

if __name__ == '__main__':
    unittest.main()