

class Solution:
    def find_element(self, arr):
        sumLeft, sumRight = 0, 0
        
        for i in range(1, len(arr)-1):
            # For first iteration, traverse the array once to get the sum of its left and its right
            if i == 1:
                # get sum of its left
                for l in range(0, i):
                    sumLeft += arr[l]
                    
                # get sum of its right
                for r in range(i + 1, len(arr)):
                    sumRight += arr[r]
            
            # For following iterations, simply subtract or add to update the sum of its left and its right
            else:
                # update sum of its left by add the previous element
                sumLeft += arr[i-1]

                # update sum of its right by subtract the current element
                sumRight -= arr[i]

            # if equals then return result
            if sumLeft == sumRight:
                return arr[i]
            
        # return not found
        return -1

import unittest
class FindElementTest(unittest.TestCase):
    def test_find_element(self):
        func = Solution().find_element
        self.assertEqual(func([2, 5, 6, 9, 10, 13, 23, 56, 77, 124]), 77)

if __name__ == "__main__":
    unittest.main()