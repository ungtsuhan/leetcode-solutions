"""
Date        : 8 August 2021
Runtime     : 60 ms, faster than 73.87% of Python3 online submissions for Two Sum.
Memory Usage: 15.3 MB, less than 41.63% of Python3 online submissions for Two Sum.
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if(complement in hashMap):
                return [hashMap[complement], i]
            else:
                hashMap[nums[i]] = i
        raise ValueError("No two sum solution")

# Unit Test
import unittest
class TwoSumCase(unittest.TestCase):
    
    def test_twoSum(self):
        func = Solution().twoSum
        self.assertEqual(func([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(func([3, 2, 4], 6), [1, 2])
        self.assertEqual(func([3, 3], 6), [0, 1])

if __name__ == '__main__':
    unittest.main()