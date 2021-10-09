"""
Date        : 9 October 2021
"""

class Solution:

    def solution(self, U, L, C):

        emptySlotRow1, emptySlotRow2, = U, L
        finalRow1 = [0 for i in range(len(C))]
        finalRow2 = [0 for i in range(len(C))]

        for i in range(len(C)):
            
            if(C[i] == 2):
                if(emptySlotRow1 > 0):
                    finalRow1[i] = 1
                    emptySlotRow1 -= 1
                else:
                    return 'IMPOSSIBLE'
                
                if(emptySlotRow2 > 0):
                    finalRow2[i] = 1
                    emptySlotRow2 -= 1
                else:
                    return 'IMPOSSIBLE'

            elif(C[i] == 1):
                if(emptySlotRow1 > 0):
                    finalRow1[i] = 1
                    emptySlotRow1 -= 1
                elif(emptySlotRow2 > 0):
                    finalRow2[i] = 1
                    emptySlotRow2 -= 1
                else:
                    return 'IMPOSSIBLE'

        result = (''.join([str(int) for int in finalRow1]) + ',' + ''.join([str(int) for int in finalRow2]))
        return result


# Unit Test
import unittest
class SolutionTestCase(unittest.TestCase):
    def test_solution(self):
        func = Solution().solution
        self.assertIn(func(3,2,[2,1,1,0,1]), ["11001,10000", "11100,10001", "10101,11000"])
        self.assertEqual(func(2,3,[0,0,1,1,2]), "IMPOSSIBLE")
        self.assertEqual(func(3,2,[2,0,2,0]), "1010,1010")

if __name__ == '__main__':
    unittest.main()