#
# @lc app=leetcode id=1530 lang=python3
#
# [1530] Number of Good Leaf Nodes Pairs
#

# @lc code=start
# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    sol1. using bfs, LCA -> TLE ...
    """

    def countPairs1(self, root: TreeNode, distance: int) -> int:
        def countPairs(self, root: TreeNode, distance: int) -> int:
            # 1. find out leaf nodes
            q = deque([root])
            leaf_nodes = []
            while q:
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                if not curr.left and not curr.right:
                    leaf_nodes.append(curr)

            # 2. Find out LCA
            def find_LCA(root, p, q):
                if not root or root == p or root == q:
                    return root
                left = find_LCA(root.left, p, q)
                right = find_LCA(root.right, p, q)
                if left and right:
                    return root
                return left if left else right

            # 3. Calculate distance
            def calculate(root, target, depth):
                if not root:
                    return -1
                if root == target:
                    return depth
                left = calculate(root.left, target, depth + 1)
                if left != -1:
                    return left
                return calculate(root.right, target, depth + 1)

            # 4. count distance btw leaf nodes
            ans = 0
            n = len(leaf_nodes)
            for i in range(n - 1):
                for j in range(i + 1, n):
                    first, second = leaf_nodes[i], leaf_nodes[j]
                    lca = find_LCA(root, first, second)
                    d = calculate(lca, first, 0) + calculate(lca, second, 0)
                    if d <= distance:
                        ans += 1
            return ans

    """
    sol2. dfs !!
    """

    def countPairs2(self, root: TreeNode, distance: int) -> int:
        def dfs(node):
            if not node:
                return []
            # leaf node
            if not node.left and node.right:
                return [1]

            # post-order traversal (left->right->node)
            left_distances = dfs(node.left)
            right_distances = dfs(node.right)

            for ld in left_distances:
                for rd in right_distances:
                    if ld + rd <= distance:
                        self.result += 1

            # calculate curr distances
            curr_dist = []
            for d in left_distances:
                if d + 1 < distance:
                    curr_dist.append(d + 1)
            for d in right_distances:
                if d + 1 < distance:
                    curr_dist.append(d + 1)

            return curr_dist

        self.result = 0
        dfs(root)
        return self.result


# @lc code=end
