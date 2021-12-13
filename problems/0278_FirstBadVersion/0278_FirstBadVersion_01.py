'''
Date        : 13 December 2021
Runtime: 20 ms, faster than 98.90% of Python3 online submissions for First Bad Version.
Memory Usage: 14.1 MB, less than 74.37% of Python3 online submissions for First Bad Version.
'''

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n: int) -> int:

        start = 0, end = n
        
        while (end - start > 1):
            mid = start + ((end - start) // 2)
            if isBadVersion(mid):
                end = mid
            else:
                start = mid
        
        return end