package leetcode;
// 700. Search in a Binary Search Tree

public class P700 {
    public TreeNode searchBST(TreeNode root, int val) {
        if (root == null) {
            return null;
        }
        return findNode(root, val);
    }

    public TreeNode findNode(TreeNode node, int val) {
        if (node == null) {
            return null;
        } else if (node.val > val) {
            return findNode(node.left, val);
        } else if (node.val < val) {
            return findNode(node.right, val);
        } else {
            return node;
        }
    }
}
