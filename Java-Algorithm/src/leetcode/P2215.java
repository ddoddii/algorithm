package leetcode;

import java.util.*;

// 2215. Find the Difference of Two Arrays
public class P2215 {
    public static List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        Set<Integer> nums1Set = new HashSet<>();
        Set<Integer> nums2Set = new HashSet<>();
        for (int num : nums1){
            nums1Set.add(num);
        }
        for (int num : nums2){
            nums2Set.add(num);
        }

        Set<Integer> nums1Diff = new HashSet<>(nums1Set);
        Set<Integer> nums2Diff = new HashSet<>(nums2Set);

        nums1Diff.removeAll(nums2Set);
        nums2Diff.removeAll(nums1Set);

        List<List<Integer>> result = new ArrayList<>();
        result.add(new ArrayList<>(nums1Diff));
        result.add(new ArrayList<>(nums2Diff));

        return result;

    }

    public static List<Integer> getElementsOnlyInFirstList(int[] nums1 , int[] nums2){
        Set<Integer> onlyInNums1 = new HashSet<>();

        Set<Integer> existsInNums2 = new HashSet<>();

        for (int num : nums2){
            existsInNums2.add(num);
        }

        for (int num : nums1){
            if (!existsInNums2.contains(num)){
                onlyInNums1.add(num);
            }
        }
        return new ArrayList<>(onlyInNums1);
    }

    public static void main(String[] args) {
        int[] nums1 = {1,2,3};
        int[] nums2 = {2,4,6};
        System.out.println(findDifference(nums1, nums2));
    }

}
