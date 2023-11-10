package leetcode;

import java.util.LinkedList;
import java.util.Queue;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

// 994. Rotting Oranges
public class P994 {
    public int orangesRotting(int[][] grid) {
        int rowSize = grid.length;
        int colSize = grid[0].length;

        Queue<int[]> q = new LinkedList<>();
        int freshOranges = 0;
        for (int i = 0; i < rowSize; i++) {
            for (int j = 0; j < colSize; j++) {
                if (grid[i][j] == 2) {
                    q.offer(new int[]{i, j});
                }
                if (grid[i][j] == 1) {
                    freshOranges++;
                }
            }
        }
        if (freshOranges == 0) {
            return 0;
        }
        return bfs(grid, q, freshOranges);

    }

    public int bfs(int[][] grid, Queue<int[]> q, int freshOranges) {
        int time = 0;
        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!q.isEmpty() && freshOranges > 0) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int[] curr = q.poll();
                for (int[] dir : directions) {
                    int newRow = curr[0] + dir[0];
                    int newCol = curr[1] + dir[1];
                    if (isValidCell(grid, newRow, newCol)) {
                        grid[newRow][newCol] = 2;
                        q.offer(new int[]{newRow, newCol});
                        freshOranges--;
                    }
                }
            }
            if (freshOranges >= 0) {
                time++;
            }
        }

        return freshOranges == 0 ? time : -1;
    }

    public boolean isValidCell(int[][] grid, int row, int col) {
        int rowSize = grid.length;
        int colSize = grid[0].length;
        if (inRange(row, rowSize) && inRange(col, colSize)) {
            return (grid[row][col] == 1);
        }
        return false;
    }

    public boolean inRange(int i, int size) {
        return (i >= 0 && i < size);
    }


    @Test
    void orangesTest() {
        P994 p994 = new P994();

        int[][] grid = {{2, 1, 1}, {1, 1, 0}, {0, 1, 1}};
        Assertions.assertEquals(4, p994.orangesRotting(grid));
    }
}
