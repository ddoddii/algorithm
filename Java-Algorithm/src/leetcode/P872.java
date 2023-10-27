package leetcode;

import java.util.ArrayList;
import java.util.List;
import java.util.Queue;

//872. Leaf-Similar Trees
public class P872 {
    boolean leafSimilar(TreeNode root1, TreeNode root2) {
        List<Integer> leaf1 = new ArrayList<>();
        List<Integer> leaf2 = new ArrayList<>();
        collectLeafNodes(root1, leaf1);
        collectLeafNodes(root2, leaf2);

        return leaf1.equals(leaf2);
    }

    void collectLeafNodes(TreeNode root, List<Integer> leaf) {
        if (root == null) {
            return;
        }
        if (root.left == null && root.right == null) {
            leaf.add(root.val);
        }
        collectLeafNodes(root.left, leaf);
        collectLeafNodes(root.right, leaf);
    }
}
