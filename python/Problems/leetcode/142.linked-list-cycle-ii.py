#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
"""
x1 : cycle start point
x2 : x1 ~ where slow & fast meet
x3 : x2 ~ where cycle start 

slow : x1 + x2
fast : x1 + x2 + x3 + x2
2(x1+x2) = x1 + 2x2 + x3
-> x1 = x3
fast, slow 가 x2 에서 만나면 fast 를 head 로 보내고, 둘다 next 해서 만나는 지점 = x1 
"""
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                fast = head
                while slow != fast:
                    fast = fast.next
                    slow = slow.next
                return fast
        return None


# @lc code=end
