package leetcode;

//547. Number of Provinces
public class P547 {
    public int findCircleNum(int[][] isConnected) {
        int nodeSize = isConnected.length;
        boolean[] visited = new boolean[nodeSize];
        int province = 0;
        for (int i = 0; i < nodeSize; i++) {
            if (!visited[i]) {
                dfs(isConnected, visited, i);
                province++;
            }
        }
        return province;
    }

    public void dfs(int[][] isConnected, boolean[] visited, int node) {
        visited[node] = true;
        for (int neighbor = 0; neighbor < isConnected.length; neighbor++) {
            if (isConnected[node][neighbor] == 1 && !visited[neighbor]) {
                dfs(isConnected, visited, neighbor);
            }
        }
    }

}
