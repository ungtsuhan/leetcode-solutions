"""
Date        : 30 January 2022
Runtime     : 1028 ms, faster than 80.77% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 25 MB, less than 95.07% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""

from typing import List 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentMaxProfit, globalMaxProfit = 0, 0
        currentLow, currentHigh = prices[0], 0
        
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                currentHigh = prices[i+1]
                currentMaxProfit = currentHigh - currentLow
                if currentMaxProfit > globalMaxProfit:
                    globalMaxProfit = currentMaxProfit
            else:
                if prices[i+1] < currentLow:
                    currentLow = prices[i+1]
                    currentMaxProfit = 0
                    
        return globalMaxProfit

import unittest

class maxProfitCase(unittest.TestCase):
    def test_maxProfit(self):
        func = Solution().maxProfit
        self.assertEqual(func([7,1,5,3,6,4]), 5)
        self.assertEqual(func([7,6,4,3,1]), 0)

if __name__ == '__main__':
    unittest.main()