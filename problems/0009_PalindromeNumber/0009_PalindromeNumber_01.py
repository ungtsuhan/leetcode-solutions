"""
Date        : 8 August 2021
Runtime     : 60 ms, faster than 66.11% of Python3 online submissions for Palindrome Number.
Memory Usage: 14.3 MB, less than 49.66% of Python3 online submissions for Palindrome Number.
"""

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        # negative number is not palindrome
        if(x < 0):
            return False
        
        # single digit number is always a palindrome
        if(x < 10):
            return True
        
        # if first digit is 0, always not a palindrome
        if(x%10 == 0):
            return False
        
        # initialization
        left, right, p = 0, 0, x

        while(right == 0 or p // right >= 100):
            right = (right * 10) + (p % 10)
            p = p // 10
        
        if(p // right >= 10):
            left = p // 10
        else: 
            left = p

        return True if (left == right) else False
        

# Unit Test
import unittest
class PanlindromeNumberCase(unittest.TestCase):
    def test_isPalindrome(self):
        func = Solution().isPalindrome
        self.assertEqual(func(121), True)
        self.assertEqual(func(-121), False)
        self.assertEqual(func(10), False)
        self.assertEqual(func(-101), False)
        self.assertEqual(func(1), True)
        self.assertEqual(func(11), True)
        self.assertEqual(func(1001), True)
        self.assertEqual(func(88888), True)
        self.assertEqual(func(21120), True)
        
if __name__ == '__main__':
    unittest.main()