package leetcode;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

// 1466. Reorder Routes to Make all Paths lead to city zero
public class P1466 {
    public int minReorder(int n, int[][] connections) {
        List<List<int[]>> graph = new ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int[] connection : connections) {
            int from = connection[0];
            int to = connection[1];
            graph.get(from).add(new int[]{to, 1}); // forward
            graph.get(to).add(new int[]{from, 0}); // reverse
        }
        boolean[] visited = new boolean[n];
        return dfs(graph, visited, 0);
    }

    public int dfs(List<List<int[]>> graph, boolean[] visited, int node) {
        visited[node] = true;
        int count = 0;
        for (int[] edge : graph.get(node)) {
            int neighbor = edge[0];
            int weight = edge[1];

            if (!visited[neighbor]) {
                count += weight;
                count += dfs(graph, visited, neighbor);
            }
        }
        return count;
    }

    public int minReorder2(int n, int[][] connections) {
        List<Set<Integer>> edges = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            edges.add(new HashSet<>());
        }
        for (int[] connection : connections) {
            edges.get(connection[0]).add(connection[1]);
            edges.get(connection[1]).add(-connection[0]);
        }
        Set<Integer> visit = new HashSet<>();
        return dfs2(0, edges, visit);

    }

    public int dfs2(int node, List<Set<Integer>> edges, Set<Integer> visit) {
        visit.add(node);
        int count = 0;
        for (int neighbor : edges.get(node)) {
            if (!visit.contains(neighbor)) {
                if (neighbor > 0) {
                    count++;
                }
                count += dfs2(Math.abs(neighbor), edges, visit);
            }
        }
        return count;
    }

    public static void main(String[] args) {
        int[][] connections = {
                {0, 1}, {1, 3}, {2, 3}, {4, 0}, {4, 5}
        };
        int n = 6;
        P1466 p1466 = new P1466();
        System.out.println(p1466.minReorder2(n, connections));

    }

}
