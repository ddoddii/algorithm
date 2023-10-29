package leetcode;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

//199. Binary Tree Right Side View
// BFS
public class P199 {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> answer = new ArrayList<>();
        Queue<TreeNode> q = new LinkedList<>();

        return traverse(root, answer, q);
    }

    List<Integer> traverse(TreeNode node, List<Integer> answer, Queue<TreeNode> q) {
        if (node == null) {
            return answer;
        }
        q.add(node);
        while (!q.isEmpty()) {
            int levelSize = q.size();
            for (int i = 0; i < levelSize; i++) {
                TreeNode currentNode = q.poll();
                if (i == levelSize - 1) {
                    answer.add(currentNode.val);
                }
                if (currentNode.left != null) {
                    q.add(currentNode.left);
                }
                if (currentNode.right != null) {
                    q.add(currentNode.right);
                }
            }
        }
        return answer;
    }
}
