package leetcode;

// 334. Increasing Triplet Subsequence
public class p334 {
    // Timeout , O(n^2)
    public static boolean increasingTriplet(int[] nums) {

        for (int i = 0 ; i < nums.length ; i++){
            int curr = nums[i];

            int maxNum = Integer.MAX_VALUE;
            int minNum = Integer.MIN_VALUE;

            for (int j = 0 ; j < i ; j++){
                if (nums[j] < maxNum) {
                    maxNum = nums[j];
                }
                System.out.println("left min num:" + maxNum);
            }
            for (int k = nums.length -1 ; k > i ; k--){
                if (nums[k] > minNum){
                    minNum = nums[k];
                }
                System.out.println("right max num: " + minNum);
            }
            if (curr > maxNum && curr < minNum){
                return true;
            }
            maxNum = Integer.MAX_VALUE;
            minNum = Integer.MIN_VALUE;

        }
        return false;
    }

    public static boolean increasingTriplet2(int[] nums) {
        int smallest = Integer.MAX_VALUE;
        int secondSmallest = Integer.MAX_VALUE;

        for (int i  = 0 ; i < nums.length ; i++) {
            if (nums[i] <= smallest){
                smallest = nums[i];
            }
            else if (nums[i] <= secondSmallest){
                secondSmallest = nums[i];
            }
            else{
                return true;
            }
        }
        return false;
    }


    public static void main(String[] args) {
        int[] nums = {0,4,2,1,0,-1,-3};

        System.out.println(increasingTriplet(nums));

    }
}
