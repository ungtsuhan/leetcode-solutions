"""
Date        : 17 Febuary 2022
Runtime     : 120 ms, faster than 73.10% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 17.7 MB, less than 74.20% of Python3 online submissions for Merge k Sorted Lists.
"""

import heapq
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    '''
    Approach: Heap
    Time Complexity: O(NlogK)
    '''

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        for idx, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap, (lst.val, idx))
        
        dummy = res = ListNode(0)
        while heap:
            _, idx = heapq.heappop(heap)
            curr = lists[idx]
            res.next = curr
            if curr.next:
                heapq.heappush(heap, (curr.next.val, idx))
                lists[idx] = lists[idx].next
            res = res.next
        return dummy.next