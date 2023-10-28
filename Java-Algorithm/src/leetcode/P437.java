package leetcode;

//437. Path Sum 3
//
public class P437 {
    private int count;

    int pathSum(TreeNode root, int targetSum) {
        iterate(root, targetSum);

        return count;
    }

    void iterate(TreeNode root, int targetSum) {
        if (root == null) {
            return;
        }
        dfsFrom(root, 0, targetSum);
        iterate(root.left, targetSum);
        iterate(root.right, targetSum);
    }

    void dfsFrom(TreeNode root, int total, int targetSum) {
        if (root == null) {
            return;
        }
        total += root.val;
        if (total == targetSum) {
            count++;
        }
        dfsFrom(root.left, total, targetSum);
        dfsFrom(root.right, total, targetSum);
    }

}
