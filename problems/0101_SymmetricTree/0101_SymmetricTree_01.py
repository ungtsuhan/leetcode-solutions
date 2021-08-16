"""
Date        : 16 August 2021
Runtime     : 32 ms, faster than 80.94% of Python3 online submissions for Symmetric Tree.
Memory Usage: 14.1 MB, less than 92.85% of Python3 online submissions for Symmetric Tree.
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        # ensure root is not none
        if not root:
            return False

        # check if left subtree and right subtree is mirror
        return self.isMirror(root.left, root.right)
            
    def isMirror(self, leftSubTree: Optional[TreeNode], rightSubTree: Optional[TreeNode]):
        
        # both leftSubTree and rightSubTree are None : means symmetry
        if not leftSubTree and not rightSubTree:
            return True
        
        # either leftSubTree or rightSubTree is None: means tree not symmetry
        if not leftSubTree or not rightSubTree:
            return False

        # value of leftSubTree not equal rightSubTree: not symmetry
        if(leftSubTree.val != rightSubTree.val):
            return False

        # when value of leftSubTree equal rightSubTree
        # recursively check the left and right child node of the current node of leftSubTree and rightSubtree
        return self.isMirror(leftSubTree.left, rightSubTree.right) and self.isMirror(leftSubTree.right, rightSubTree.left)

# Unit Test
import unittest
class isSymmetricCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_isSymmetric(self):
        func = Solution().isSymmetric
        
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(2)
        p.left.left = TreeNode(3)
        p.left.right = TreeNode(4)
        p.right.left = TreeNode(4)
        p.right.right = TreeNode(3)

        self.assertEqual(func(p), True)

        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(2)
        p.left.right = TreeNode(3)
        p.right.right = TreeNode(3)

        self.assertEqual(func(p), False)

if __name__ == '__main__':
    unittest.main()