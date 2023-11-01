package leetcode;

import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;

// 1161. Maximum Level Sum of a Binary Tree
public class P1161 {
    public int maxLevelSum(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<>();
        int sum;
        int level = 0;
        int maxSum = Integer.MIN_VALUE;
        Map<Integer, Integer> levelSum = new HashMap<>();
        q.add(root);
        while (!q.isEmpty()) {
            sum = 0;
            level++;
            int levelSize = q.size();
            for (int i = 0; i < levelSize; i++) {
                TreeNode currNode = q.poll();
                sum += currNode.val;
                if (currNode.left != null) {
                    q.add(currNode.left);
                }
                if (currNode.right != null) {
                    q.add(currNode.right);
                }
            }
            levelSum.put(level, sum);
        }
        return getMinlevelWithMaxSum(levelSum);

    }

    public int getMinlevelWithMaxSum(Map<Integer, Integer> levelSum) {
        Map.Entry<Integer, Integer> maxEntry = levelSum.entrySet().stream()
                .max(Comparator.comparing(Map.Entry::getValue))
                .orElse(null);

        return maxEntry.getKey();
    }


}
