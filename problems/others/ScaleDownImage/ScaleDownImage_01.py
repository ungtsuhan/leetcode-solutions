"""
Date        : 12 August 2021
"""

class Solution:
    def scaleDownImage(self, length, width, maxRes):
        
        if(length > width):
            factorLength = length / width
            factorWidth = 1
        else:
            factorLength = 1
            factorWidth = width / length
        
        newLength = length
        newWidth = width

        currentRes = newLength * newWidth
        while currentRes > maxRes:
            newLength = newLength - factorLength
            newWidth = newWidth - factorWidth
            currentRes = newLength * newWidth
        print(newLength, newWidth)
        return (newLength, newWidth)
    
# Unit Test
import unittest
class ScaleDownImageCase(unittest.TestCase):
    def test_scaleDownImage(self):
        func = Solution().scaleDownImage
        self.assertEqual(func(50, 100, 1000), (22,44))
        self.assertEqual(func(100, 50, 1000), (44,22))
    
if __name__ == '__main__':
    unittest.main()