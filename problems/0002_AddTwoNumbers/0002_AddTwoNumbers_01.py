"""
Date        : 31 January 2022
Runtime     : 92 ms, faster than 40.03% of Python3 online submissions for Add Two Numbers.
Memory Usage: 14 MB, less than 94.39% of Python3 online submissions for Add Two Numbers.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = n = ListNode('#')
        carry = 0
        while l1 or l2 or carry != 0:
            currentSum = carry
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            currentSum = carry + val1 + val2
            carry = currentSum // 10
            n.next = ListNode(currentSum % 10)
            n = n.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next