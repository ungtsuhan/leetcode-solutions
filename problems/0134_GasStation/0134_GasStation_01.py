"""
Date        : 8 October 2021
Runtime     : 7308 ms, faster than 5.01% of Python3 online submissions for Gas Station.
Memory Usage: 17.8 MB, less than 22.42% of Python3 online submissions for Gas Station.
"""

class Solution:
    
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    
    def CanCompleteCircuitBruteForce(self, gas, cost):
        # going through each station as starting point
        for start in range(len(gas)):
            feasible = True
            tank = 0
            # check whether can go through whole circuit with this starting point
            for i in range(start, len(gas) + start):
                station = i % len(gas)
                tank += (gas[station] - cost[station])
                if tank < 0:
                    feasible = False
                    break
            if feasible:
                return start
        return -1

# Unit Test
import unittest
class CanCompleteCircuitCase(unittest.TestCase):
    def test_canCompleteCircuit(self):
        func = Solution().CanCompleteCircuitBruteForce
        self.assertEqual(func([1,2,3,4,5], [3,4,5,1,2]), 3)
        self.assertEqual(func([2,3,4], [3,4,3]), -1)

if __name__ == '__main__':
    unittest.main()