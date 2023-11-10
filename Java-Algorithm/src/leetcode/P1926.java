package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Set;

// 1926. Nearest Exit from Entrance in Maze
public class P1926 {
    public int nearestExit(char[][] maze, int[] entrance) {
        Set<List<Integer>> borderCells = findBorderCell(maze);
        return 0;
    }

    public int bfs(char[][] maze, int[] entrance) {
        Queue<List<Integer>> q = new LinkedList<>();
        Set<List<Integer>> visited = new HashSet<>();
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        q.offer(Arrays.asList(entrance[0], entrance[1], 0));
        visited.add(Arrays.asList(entrance[0], entrance[1]));

        while (!q.isEmpty()) {
            List<Integer> current = q.poll();
            int row = current.get(0);
            int col = current.get(1);
            int distance = current.get(2);
            if (isExit(maze, row, col)) {
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
        if (maze[row][col] == '.' && isRowEnd(row, rowSize)) {
            return true;
        } else if (maze[row][col] == '.' && isColEnd(col, colSize)) {
            return true;
        }
        return false;
    }

    public boolean isValidCell(char[][] maze, int row, int col, Set<List<Integer>> visited) {
        int rowSize = maze.length;
        int colSize = maze[0].length;
        if (!visited.contains(Arrays.asList(row, col))) {
            return (maze[row][col] == '.' && inRange(row, rowSize) && inRange(col, colSize));
        }
        return false;
    }

    public boolean inRange(int i, int size) {
        return (i >= 0 && i <= size - 1);
    }


    public Set<List<Integer>> findBorderCell(char[][] maze) {
        int rowSize = maze.length;
        int colSize = maze[0].length;
        Set<List<Integer>> borderCells = new HashSet<>();
        addRowEndCell(maze, borderCells, rowSize, colSize);
        addColEndCell(maze, borderCells, rowSize, colSize);
        return borderCells;
    }

    public void addRowEndCell(char[][] maze, Set<List<Integer>> borderCells, int rowSize, int colSize) {
        for (int i = 0; i < rowSize; i++) {
            for (int j = 0; j < colSize; j++) {
                if (maze[i][j] == '.' && isRowEnd(i, rowSize)) {
                    List<Integer> pair = new ArrayList<>();
                    pair.add(i);
                    pair.add(j);
                    borderCells.add(pair);
                }
            }
        }
    }

    public void addColEndCell(char[][] maze, Set<List<Integer>> borderCells, int rowSize, int colSize) {
        for (int i = 0; i < rowSize; i++) {
            for (int j = 0; j < colSize; j++) {
                if (maze[i][j] == '.' && isColEnd(j, colSize)) {
                    List<Integer> pair = new ArrayList<>();
                    pair.add(i);
                    pair.add(j);
                    borderCells.add(pair);
                }
            }
        }
    }

    public boolean isRowEnd(int i, int rowSize) {
        return (i == 0 || i == rowSize - 1);
    }

    public boolean isColEnd(int j, int colSize) {
        return (j == 0 || j == colSize - 1);
    }


    public static void main(String[] args) {
        char[][] maze = {
                {'+', '+', '.', '+'},
                {'.', '.', '.', '+'},
                {'+', '+', '+', '.'}
        };
        int[] entrance = {1, 2};

        P1926 p1926 = new P1926();

    }


}
