"""
Date        : 15 August 2021
Runtime     : 32 ms, faster than 57.39% of Python3 online submissions for Same Tree.
Memory Usage: 14.3 MB, less than 63.02% of Python3 online submissions for Same Tree.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        # both p and q are None : means tree has ended
        if not p and not q:
            return True
        
        # one of p or q is None: means tree not same
        if not p or not q:
            return False
        
        # check value of p and q is same 
        if p.val != q.val:
            return False

        # check left and right child node recursively
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Unit Test
import unittest
class isSameTreeCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_isSameTree(self):
        func = Solution().isSameTree

        self.assertEqual(func(None, None), True)

        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(3)
        p.left.left = TreeNode(2)
        p.left.right = TreeNode(2)
        p.right.right = TreeNode(3)  

        q = TreeNode(1)
        q.left = TreeNode(2)
        q.right = TreeNode(3)
        q.left.left = TreeNode(2)
        q.left.right = TreeNode(2)
        q.right.right = TreeNode(3)     

        self.assertEqual(func(p, q), True)

        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(1)

        q = TreeNode(1)
        q.left = TreeNode(1)
        q.right = TreeNode(2)

        self.assertEqual(func(p, q), False)

        p = TreeNode(1)
        p.left = TreeNode(2)

        q = TreeNode(1)
        q.right = TreeNode(2)

        self.assertEqual(func(p, q), False)    

if __name__ == '__main__':
    unittest.main()