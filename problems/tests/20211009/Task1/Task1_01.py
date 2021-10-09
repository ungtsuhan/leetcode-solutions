"""
Date        : 9 October 2021
"""

class Solution:

    def solution(self, B):
        
        numberOfShip = [0,0,0]
        board = B
        occupied = {}

        def CheckGotBoat(row, column):
            if(row < 0 or column < 0 or row >= len(board) or column >= len(board[row])):
                return False
            elif(board[row][column] == "#" and (row, column) not in occupied):
                return True
            else:
                return False
        
        def ReturnAdjacentBoat(row,column):
            adjBoatCount = 0
            adjBoat = []
            if(CheckGotBoat(row+1, column)):
                adjBoatCount+=1
                adjBoat.append((row+1, column))
            if(CheckGotBoat(row-1, column)):
                adjBoatCount+=1
                adjBoat.append((row-1, column))
            if(CheckGotBoat(row, column+1)):
                adjBoatCount+=1
                adjBoat.append((row, column+1))
            if(CheckGotBoat(row, column-1)):
                adjBoatCount+=1
                adjBoat.append((row, column-1))
            return adjBoatCount, adjBoat
        
        for rowIndex in range(len(board)):
            
            for columnIndex in range(len(board[rowIndex])):

                if(board[rowIndex][columnIndex] == '#' and (rowIndex, columnIndex) not in occupied):
                    
                    occupied[(rowIndex,columnIndex)] = True
                    adjacentCount = 1
                    
                    (adjCount, adjBoats) = ReturnAdjacentBoat(rowIndex, columnIndex)
                    
                    for p in (range(adjCount)):
                        (adjBoatsRow,adjBoatsColumn) = adjBoats[p]
                        occupied[(adjBoatsRow,adjBoatsColumn)] = True
                        adjacentCount += 1

                    if(adjCount == 1):
                        (adjBoatsRow,adjBoatsColumn) = adjBoats[0]
                        (nextAdjCount,nextAdjBoats) = ReturnAdjacentBoat(adjBoatsRow, adjBoatsColumn)
                        if(nextAdjCount > 0):
                            (nextAdjBoatsRow,nextAdjBoatsColumn) = nextAdjBoats[0]
                            occupied[(nextAdjBoatsRow,nextAdjBoatsColumn)] = True
                            adjacentCount += 1    

                    if(adjacentCount == 1):
                        numberOfShip[0] = numberOfShip[0] + 1
                    elif(adjacentCount == 2):
                        numberOfShip[1] = numberOfShip[1] + 1
                    elif(adjacentCount == 3):
                        numberOfShip[2] = numberOfShip[2] + 1
                    
        return numberOfShip

# Unit Test
import unittest
class SolutionTestCase(unittest.TestCase):
    def test_solution(self):
        func = Solution().solution
        self.assertEqual(func(['.##.#','#.#..','#...#','#.##.']), [2,1,2])
        self.assertEqual(func(['.#..#','##..#','...#.']), [1,1,1])
        self.assertEqual(func(['##.','#.#','.##']), [0,0,2])
        self.assertEqual(func(['...','...','...']), [0,0,0])

if __name__ == '__main__':
    unittest.main()
    