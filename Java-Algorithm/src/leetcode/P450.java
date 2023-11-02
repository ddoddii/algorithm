package leetcode;

// P450. Delete Node in a BST
// 1102 : ‼️
public class P450 {
    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) {
            return null;
        }
        if (root.val > key) {
            root.left = deleteNode(root.left, key);
        } else if (root.val < key) {
            root.right = deleteNode(root.right, key);
        } else {
            // delete
            if (root.left == null) {
                return root.right;
            } else if (root.right == null) {
                return root.left;
            } else {
                // find min from right subtree
                TreeNode minNode = findMin(root.right);
                root.val = minNode.val;
                // delete duplicate
                root.right = deleteNode(root.right, minNode.val);
            }
        }
        return root;
    }

    public TreeNode findMin(TreeNode node) {
        while (node.left != null) {
            node = node.left;
        }
        return node;
    }
}

