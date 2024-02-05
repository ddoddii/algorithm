#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        while curr and curr.next:
            # save pairs
            nxtPair = curr.next.next
            second = curr.next

            # reverse current pair
            second.next = curr
            prev.next = second
            curr.next = nxtPair

            # update pair
            prev = curr
            curr = nxtPair
        return dummy.next


# @lc code=end
