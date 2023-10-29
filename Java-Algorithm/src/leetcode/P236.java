package leetcode;

//236. Lowest Common Ancestor
public class P236 {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        return traverse(root, p, q);
    }

    TreeNode traverse(TreeNode node, TreeNode p, TreeNode q) {
        if (node == null) {
            return null;
        }
        if (node == p || node == q) {
            return node;
        }
        TreeNode left = traverse(node.left, p, q);
        TreeNode right = traverse(node.right, p, q);

        if (left != null && right != null) {
            return node;
        } else if (left != null) {
            return left; // 다른 노드는 left 의 subtree 안에 있음
        } else {
            return right; // 다른 노드는 right 의 subtree 안에 있음
        }
    }

}
