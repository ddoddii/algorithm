package leetcode;

import java.util.Arrays;

import static java.lang.Double.sum;

// 643. Maximum Average Subarray 1
public class P643 {
    //sol1 . time limit O(n^2)
    public static double findMaxAverage(int[] nums, int k) {
        int iter = nums.length - k + 1;
        double maxAvg  = Integer.MIN_VALUE;
        for (int i = 0 ; i < iter ; i++){
            int[] subseq = Arrays.copyOfRange(nums, i,i +k);
            int sum = 0;
            for (int num : subseq){
                sum += num;
            }

            double avg = (double) sum / k;
            if (avg > maxAvg) {
                maxAvg = avg;
            }

        }
        return maxAvg;

    }

    //sol2. Using sliding window
    public static double findMaxAverage2(int[] nums, int k){
        int sum = 0;
        for (int i = 0 ; i < k ; i++){
            sum += nums[i];
        }
        int maxSum = sum;

        for (int i = k ; i < nums.length ; i++){
            sum = sum - nums[i-k] + nums[i];
            maxSum = Math.max(sum , maxSum);
        }
        double avg = (double) maxSum / k;
        return avg;

    }

    public static void main(String[] args) {
        int[] nums = {1,12,-5,-6,50,3};
        int k = 1;
        System.out.println(findMaxAverage2(nums, k));
    }

}
