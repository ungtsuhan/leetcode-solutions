"""
Date        : 16 August 2021
Runtime     : 44 ms, faster than 44.48% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 16.1 MB, less than 40.71% of Python3 online submissions for Maximum Depth of Binary Tree.
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        # add 1 to current node and recursively find the maxDepth of left child node of current node
        left = self.maxDepth(root.left) + 1
        
        # add 1 to current node and recursively find the maxDepth of right child node of current node
        right = self.maxDepth(root.right) + 1
        
        # compare and find the max between left subtree and right subtree
        result = max(left, right)
        
        return result

# Unit Test
import unittest
class maxDepthCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_maxDepth(self):
        func = Solution().maxDepth
        
        p = TreeNode(1)
        p.left = TreeNode(9)
        p.right = TreeNode(20)
        p.right.left = TreeNode(15)
        p.right.right = TreeNode(7)

        self.assertEqual(func(p), 3)

        p = TreeNode(1)
        p.right = TreeNode(2)

        self.assertEqual(func(p), 2)

        p = None

        self.assertEqual(func(p), 0)

        p = TreeNode(0)

        self.assertEqual(func(p), 1)

if __name__ == '__main__':
    unittest.main()