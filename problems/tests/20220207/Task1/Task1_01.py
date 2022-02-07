"""
Date        : 7 Febuary 2022
"""

class Solution:
    def calculatePrimeNumbers(self, num):
        arr = []
        for n in range(2, num + 1):
            for i in range(2, n):
                if (n % i) == 0:
                    break
            else:
                arr.append(n)
        return arr

import unittest

class calculatePrimeNumbersCase(unittest.TestCase):
    def test_calculatePrimeNumbers(self):
        func = Solution().calculatePrimeNumbers
        self.assertEquals(func(11), [2, 3, 5, 7, 11])
        self.assertEquals(func(4), [2, 3])
        self.assertEquals(func(2), [2])

if __name__ == "__main__":
    unittest.main()