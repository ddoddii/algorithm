#
# @lc app=leetcode id=2816 lang=python3
#
# [2816] Double a Number Represented as a Linked List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def swap(head):
            nxt = None
            curr = head
            while curr:
                temp = curr.next
                curr.next = nxt
                nxt = curr
                curr = temp
            return nxt

        tail = swap(head)
        curr = tail
        carry = 0
        while curr:
            total = curr.val * 2 + carry
            carry = total // 10
            curr.val = total % 10
            prev = curr
            curr = curr.next
        if carry:
            prev.next = ListNode(carry)

        tail = swap(tail)

        return tail

    def doubleIt2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val > 4:
            head = ListNode(0, head)
        node = head
        while node:
            node.val = (node.val * 2) % 10
            if node.next and node.next.val > 4:
                node.val += 1
            node = node.next
        return head


# @lc code=end
