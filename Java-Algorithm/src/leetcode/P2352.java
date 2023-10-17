package leetcode;

import java.util.*;

// 2352. Equal Row and Column pairs
public class P2352 {
    public static int equalPairs(int[][] grid) {
        Map<String, String> rowMap = new HashMap<>();
        Map<String, String> colMap = new HashMap<>();
        for (int i = 0 ; i < grid.length ; i++){
            StringBuilder sb1 = new StringBuilder();
            StringBuilder sb2 = new StringBuilder();
            for (int j = 0; j < grid[i].length ; j++) {
                sb1.append(grid[i][j]).append(" ");
                sb2.append(grid[j][i]).append(" ");
            }
            rowMap.put("r" + i, String.valueOf(sb1));
            colMap.put("c" + i, String.valueOf(sb2));
        }

        int pair = 0;

        for (String row : rowMap.values()){
            for (String col : colMap.values()){
                if (Objects.equals(col, row)) pair++;
            }

        }
        return pair;

    }

    public static int equalPairs2(int[][] grid){
        Map<String, Integer> cnt = new HashMap<>();
        for (int[] row : grid){
            String key = Arrays.toString(row);
            cnt.put(key, 1 + cnt.getOrDefault(key, 0));
        }
        int pair = 0;
        int n = grid.length;
        for (int i = 0 ; i < n ; i++){
            int[] col = new int[n];
            for (int j = 0 ; j < n ; j++){
                col[j] = grid[j][i];
            }
            pair += cnt.getOrDefault(Arrays.toString(col), 0);
        }
        return pair;
    }

    public static void main(String[] args) {
        int[][] grid = {{11,1},{1,11}};
        System.out.println(equalPairs2(grid));


    }
}
