"""
Date        : 6 Febuary 2022
Runtime     : 1585 ms, faster than 5.77% of Python3 online submissions for Gas Station.
Memory Usage: 28.3 MB, less than 6.44% of Python3 online submissions for Gas Station.
"""

class Solution:
    
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    
    def CanCompleteCircuit(self, gas, cost):
        remaining = 0
        candidtate = 0
        for i in range(len(gas)):
            remaining += gas[i] - cost[i]
            if remaining < 0:
                remaining = 0
                candidtate = i + 1
        prev_remaining = sum(gas[:candidtate]) - sum(cost[:candidtate])
        if candidtate == len(gas) or remaining + prev_remaining < 0:
            return -1
        else:
            return candidtate

# Unit Test
import unittest
class CanCompleteCircuitCase(unittest.TestCase):
    def test_canCompleteCircuit(self):
        func = Solution().CanCompleteCircuit
        self.assertEqual(func([1,2, 3,4,5], [3,4,5,1,2]), 3)
        self.assertEqual(func([2,3,4], [3,4,3]), -1)

if __name__ == '__main__':
    unittest.main()