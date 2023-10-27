package leetcode;

//1448. Count Good Nodes in Binary Tree
public class P1448 {
    private int goodNodeCount = 0;

    public int goodNodes(TreeNode root) {
        dfs(root, Integer.MIN_VALUE);
        return goodNodeCount;
    }

    void dfs(TreeNode root, int maxSoFar) {
        if (root == null) {
            return;
        }
        if (root.val >= maxSoFar) {
            goodNodeCount++;
            maxSoFar = root.val;
        }
        dfs(root.left, maxSoFar);
        dfs(root.right, maxSoFar);

    }
}
