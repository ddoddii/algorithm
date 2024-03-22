#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Slow & Fast Pointer
    """

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow : middle of linked list
        prev = None
        while slow:
            curr = slow
            slow = slow.next
            curr.next = prev
            prev = curr

        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next

        return True


# @lc code=end
