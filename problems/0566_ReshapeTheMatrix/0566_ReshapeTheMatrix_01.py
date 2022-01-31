"""
Date        : 31 January 2022
Runtime     : 132 ms, faster than 35.28% of Python3 online submissions for Reshape the Matrix.
Memory Usage: 14.8 MB, less than 85.65% of Python3 online submissions for Reshape the Matrix.
"""

from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        N, M = len(mat), len(mat[0])
        if N*M != r*c:
            return mat
        
        output = [[0 for _ in range(c)] for _ in range(r)]
        
        k=0
        for i in range(N):
            for j in range(M):
                output[k//c][k%c] = mat[i][j]
                k+=1
        return output

import unittest

class matrixReshapeCase(unittest.TestCase):
    def test_matrixReshape(self):
        func = Solution().matrixReshape
        self.assertEqual(func([[1,2],[3,4]], 1, 4), [[1,2,3,4]])
        self.assertEqual(func([[1,2],[3,4]], 2, 4), [[1,2],[3,4]])
       
if __name__ == "__main__":
    unittest.main()