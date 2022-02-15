"""
Date        : 7 Febuary 2022
"""

class Solution:
    def minRoutes(self, pickLoc, baseX0, baseY0):
        pickLoc.append([baseX0, baseY0])
        slopeHashMap = {}
        for i in range(len(pickLoc)):
            for j in range(i, len(pickLoc)):
                if i == j:
                    break
                print(i, j)
        return 0

        
import unittest

class minRoutesCase(unittest.TestCase):
    def test_minRoutes(self):
        func = Solution().minRoutes
        self.assertEquals(func([[1,1], [-1,1], [2,3]], 0, 0), 3)

if __name__ == "__main__":
    unittest.main()