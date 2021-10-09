"""
Date        : 9 October 2021
"""

class Solution:

    def solution(self, A, S):
        
        possible = 0
        for i in range(len(A)):
            sum = 0
            count = 0
            for j in range(i, len(A)):
                sum += A[j]
                count += 1
                if(sum / (count) == S):
                    possible += 1

        return possible

# Unit Test
import unittest
class SolutionTestCase(unittest.TestCase):
    def test_solution(self):
        func = Solution().solution
        self.assertEqual(func([2,1,3], 2), 3)
        self.assertEqual(func([0,4,3,-1], 2), 2)
        self.assertEqual(func([2,1,4], 3), 0)

if __name__ == '__main__':
    unittest.main()