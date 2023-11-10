package leetcode;

import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Set;

// 1926. Nearest Exit from Entrance in Maze
public class P1926 {
    public int nearestExit(char[][] maze, int[] entrance) {
        Queue<List<Integer>> q = new LinkedList<>();
        Set<List<Integer>> visited = new HashSet<>();
        q.offer(Arrays.asList(entrance[0], entrance[1], 0));
        visited.add(Arrays.asList(entrance[0], entrance[1]));
        return bfs(maze, entrance, q, visited);
    }

    public int bfs(char[][] maze, int[] entrance, Queue<List<Integer>> q, Set<List<Integer>> visited) {
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        while (!q.isEmpty()) {
            List<Integer> current = q.poll();
            int row = current.get(0);
            int col = current.get(1);
            int distance = current.get(2);
            if (isExit(maze, row, col) && isNotEntrance(entrance, row, col)) {
                return distance;
            }
            for (int[] dir : directions) {
                int newRow = row + dir[0];
                int newCol = col + dir[1];
                if (isValidCell(maze, newRow, newCol, visited)) {
                    q.offer(Arrays.asList(newRow, newCol, distance + 1));
                    visited.add(Arrays.asList(newRow, newCol));
                }
            }

        }
        return -1;
    }

    public boolean isExit(char[][] maze, int row, int col) {
        int rowSize = maze.length;
        int colSize = maze[0].length;
        if (maze[row][col] == '.' && isEnd(row, rowSize) ) {
            return true;
        } else if (maze[row][col] == '.' && isEnd(col, colSize) ) {
            return true;
        }
        return false;
    }

    public boolean isNotEntrance(int[] entrance, int row, int col){
        return (entrance[0] != row || entrance[1] != col);
    }

    public boolean isValidCell(char[][] maze, int row, int col, Set<List<Integer>> visited) {
        int rowSize = maze.length;
        int colSize = maze[0].length;
        if (inRange(row, rowSize) && inRange(col, colSize)) {
            return (maze[row][col] == '.' && !visited.contains(Arrays.asList(row, col)));
        }
        return false;
    }

    public boolean inRange(int i, int size) {
        return (i >= 0 && i <= size - 1);
    }

    public boolean isEnd(int i, int size) {
        return (i == 0 || i == size - 1);
    }

    public static void main(String[] args) {
        char[][] maze = {
                {'+', '+', '+'},
                {'.', '.', '.'},
                {'+', '+', '+'}
        };
        int[] entrance = {1, 0};

        P1926 p1926 = new P1926();
        System.out.println(p1926.nearestExit(maze, entrance));

    }


}
