"""
Date        : 18 August 2021
Runtime     : 4 ms, faster than 59.64% of Python3 online submissions for Path Sum.
Memory Usage: 15.9 MB, less than 58.07% of Python3 online submissions for Path Sum.
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        leftHasPathSum, rightHasPathSum = False, False

        # get the value of diff between target sum and value of current node
        subSum = targetSum - root.val
 
        # when reach a leaf node, and the subSum to meet targetSum is 0, targetSum is met
        if(not root.left and not root.right and subSum == 0):
            return True

        # if not leaf node, recursively check hasPathSum of the left and right child node
        if root.left:
            leftHasPathSum = self.hasPathSum(root.left, subSum)
        if root.right:
            rightHasPathSum = self.hasPathSum(root.right, subSum)

        # return true either left path or right path has path sum
        return leftHasPathSum or rightHasPathSum

# Unit Test
import unittest
class hasPathSumTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_hasPathSum(self):
        func = Solution().hasPathSum

        p = TreeNode(5)
        p.left = TreeNode(4)
        p.left.left = TreeNode(11)
        p.left.left.left = TreeNode(7)
        p.left.left.right = TreeNode(2)
        p.right = TreeNode(8)
        p.right.left = TreeNode(13)
        p.right.right = TreeNode(4)
        p.right.right.right = TreeNode(1)

        self.assertEqual(func(p, 22), True)

        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(3)

        self.assertEqual(func(p, 5), False)

        p = TreeNode(1)
        p.left = TreeNode(2)

        self.assertEqual(func(p, 0), False)

        p = None

        self.assertEqual(func(p, 1), False)

if __name__ == '__main__':
    unittest.main()