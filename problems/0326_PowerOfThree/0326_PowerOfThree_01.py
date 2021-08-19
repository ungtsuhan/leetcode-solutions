"""
Date        : 19 August 2021
Runtime     : 84 ms, faster than 45.84% of Python3 online submissions for Power of Three.
Memory Usage: 14.3 MB, less than 16.96% of Python3 online submissions for Power of Three.
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while True:
            if n < 1:
                return False
            if n == 1:
                return True
            if n%3 != 0:
                return False
            else:
                n =  n / 3
            
# Unit Test
import unittest
class IsPowerOfThreeCase(unittest.TestCase):
    def test_isPowerOfThree(self):
        func = Solution().isPowerOfThree
        self.assertEqual(func(27), True)
        self.assertEqual(func(0), False)
        self.assertEqual(func(9), True)
        self.assertEqual(func(45), False)
        self.assertEqual(func(1), True)

if __name__ == '__main__':
    unittest.main()