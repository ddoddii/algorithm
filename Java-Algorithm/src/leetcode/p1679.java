package leetcode;

import java.util.*;

//1679. Max number of k-sum pairs
public class p1679 {
    public static int maxOperations(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        int count = 0;

        for (int num : nums){
            int complement = k - num;
            if (map.getOrDefault(complement, 0) > 0){
                count++;
                map.put(complement, map.get(complement) -1);
            }
            else {
                map.put(num , map.getOrDefault(num,0) + 1);
            }

        }
        return count;

    }

    public static void main(String[] args) {
        int[] nums = {1,2,3,4};
        int k = 5;
        System.out.println(maxOperations(nums, k));
    }
}
