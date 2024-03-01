#
# @lc app=leetcode id=1609 lang=python3
#
# [1609] Even Odd Tree
#

# @lc code=start
# Definition for a binary tree node.

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:

        def is_even(num: int) -> bool:
            return num % 2 == 0

        def is_increasing(level: List[int]) -> bool:
            for i in range(len(level) - 1):
                if level[i] >= level[i + 1]:
                    return False
            return True

        def is_decreasing(level: List[int]) -> bool:
            for i in range(len(level) - 1):
                if level[i] <= level[i + 1]:
                    return False
            return True

        def odd_level(level: List[int]) -> bool:
            for n in level:
                if not is_even(n):
                    return False
            return is_decreasing(level)

        def even_level(level: List[int]) -> bool:
            for n in level:
                if is_even(n):
                    return False
            return is_increasing(level)

        if not root or is_even(root.val):
            return False
        q = [root]
        curr_level = 0
        while q:
            level = []
            level_size = len(q)
            for _ in range(level_size):
                curr = q.pop(0)
                level.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            # odd level - even number, decreasing
            if curr_level % 2 == 1:
                if not odd_level(level):
                    return False

            # even level - odd number, increasing
            else:
                if not even_level(level):
                    return False
            curr_level += 1
        return True

    """
    - bit operations for even / odd
    """

    def isEvenOddTree2(self, root: Optional[TreeNode]) -> bool:
        bit_level = 1
        q = [root] if root else []
        while q:
            for i in range(len(q)):
                # if x & 1 == 1 : odd number ->  x & 1 == True : odd, x & 1 == False : even
                if q[i].val & 1 != bit_level:
                    return False
                if i < len(q) - 1 and (
                    (q[i].val > q[i + 1].val) == bool(bit_level)
                    or q[i].val == q[i + 1].val
                ):
                    return False
            # flip the bit level
            bit_level ^= 1
            q = [node for n in q for node in (n.left, n.right) if node]
        return True


# @lc code=end
