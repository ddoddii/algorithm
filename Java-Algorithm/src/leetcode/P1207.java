package leetcode;

import java.util.*;

// 1207. Unique number of occurences
public class P1207 {
    public static boolean uniqueOccurences(int[] arr){
        Map<Integer, Integer> numCounts = new HashMap<>();
        Set<Integer> uniqueNums = new HashSet<>();
        for (int num : arr){
            Integer count = numCounts.getOrDefault(num , 0);
            numCounts.put(num , count+1);
        }
        uniqueNums.addAll(numCounts.values());
        return (uniqueNums.size() == numCounts.values().size());
    }

    public static void main(String[] args) {
        int[] arr = {-3,0,1,-3,1,1,1,-3,10,0};
        System.out.println(uniqueOccurences(arr));
    }
}
