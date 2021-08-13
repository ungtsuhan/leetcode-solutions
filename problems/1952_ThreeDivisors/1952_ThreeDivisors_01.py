"""
Date        : 13 August 2021
Runtime     : 44 ms, faster than 32.16% of Python3 online submissions for Three Divisors.
Memory Usage: 14.3 MB, less than 43.36% of Python3 online submissions for Three Divisors.
"""

class Solution:
    def isThree(self, n: int) -> bool:
        
        if(n < 1 or n > 104):
            return False
        
        numOfDivisor, currentDivisor = 0, 1
        
        while currentDivisor <= n:
            if n % currentDivisor == 0:
                numOfDivisor += 1

            if(numOfDivisor) > 3:
                return False
            
            currentDivisor += 1

        return True if (numOfDivisor == 3) else False

# Unit Test
import unittest
class IsThreeTestCase(unittest.TestCase):
    def test_isThree(self):
        func = Solution().isThree
        self.assertEqual(func(2), False)
        self.assertEqual(func(12), False)

if __name__ == '__main__':
    unittest.main()