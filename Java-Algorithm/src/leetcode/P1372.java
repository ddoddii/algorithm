package leetcode;

//1372. Longest ZigZag in a Binary Tree
public class P1372 {
    private int maxLength = 0;

    public int longestZigZag(TreeNode root) {
        if (root == null) {
            return 0;
        }
        zigzagTraversal(root, 0, 1);
        zigzagTraversal(root, 0, -1);
        return maxLength;
    }

    void zigzagTraversal(TreeNode node, int length, int direction) {
        if (node == null) {
            return;
        }
        maxLength = Math.max(maxLength, length);

        if (direction == 1) {
            zigzagTraversal(node.left, 1, 1);
            zigzagTraversal(node.right, length + 1, -1);
        } else {
            zigzagTraversal(node.right, 1, -1);
            zigzagTraversal(node.left, length + 1, 1);
        }

    }

}
