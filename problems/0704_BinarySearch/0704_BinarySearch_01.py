'''
Date        : 9 October 2021
Runtime     : 244 ms, faster than 51.11% of Python3 online submissions for Binary Search.
Memory Usage: 15.7 MB, less than 28.21% of Python3 online submissions for Binary Search.
'''
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        if(target == nums[low]):
            return low
        elif(target == nums[high]):
            return high
        while high-low > 1:

            mid = (high+low)//2
            if(target > nums[mid]):
                low = mid
            elif(target < nums[mid]):
                high = mid
            else:
                return mid
            
        return -1

# Unit Test
import unittest
class SearchTestCase(unittest.TestCase):
    def test_search(self):
        func = Solution().search
        self.assertEqual(func([-1,0,3,5,9,12], 9), 4)
        self.assertEqual(func([-1,0,3,5,9,12], 2), -1)

if __name__ == '__main__':
    unittest.main()