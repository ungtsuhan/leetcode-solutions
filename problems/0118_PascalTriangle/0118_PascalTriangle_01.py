"""
Date        : 31 January 2022
Runtime     : 27 ms, faster than 90.45% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 13.9 MB, less than 98.99% of Python3 online submissions for Pascal's Triangle.
"""

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []
        h = 0
        while h < numRows:
            row = []
            c = 0
            while c < h+1:
                if c == 0 or c == h:
                    row.append(1)
                else:
                    row.append(output[h-1][c%h - 1] + output[h-1][c%h])
                c+=1
            output.append(row)
            h+=1
        return output

import unittest

class generateCase(unittest.TestCase):
    def test_generate(self):
        func = Solution().generate
        self.assertEqual(func(5), [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]])
        self.assertEqual(func(1), [[1]])

if __name__ == "__main__":
    unittest.main()