"""
Date        : 15 Febuary 2022
Runtime     : 112 ms, faster than 80.34% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 17.7 MB, less than 86.17% of Python3 online submissions for Merge k Sorted Lists.
"""

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    '''
    Approach: Divide and Conquer
    Time Complexity: O(NlogK)
    '''

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
         # if list is null or length of list is 0
        if not lists or len(lists) == 0:
            # return empty linked list
            return None
        
        # keep doing merge sort until there is only one element in the list
        while len(lists) > 1:
            mergedLists = []
            
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None # may be out of bound
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]
    
    # refer 0021 merge two sorted lists
    def mergeList(self, l1: ListNode, l2: ListNode):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
            
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
            
        return dummy.next