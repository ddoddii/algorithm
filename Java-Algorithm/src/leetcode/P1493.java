package leetcode;

// 1493. Longest Subarray of 1's After deleting one element
public class P1493 {
    public static int longestSubarray(int[] nums) {
        int left = 0;
        int right= 0;
        int max = 0;
        int countZero = 0;

        while(right < nums.length){
            if (nums[right] == 0){
                countZero++;
            }
            if (countZero > 1){
                if (nums[left] == 0){
                    countZero--;
                }
                left++;
            }
            max = Math.max(max, right - left + 1);
            right++;
        }
        return max > 0 ? max - 1 : 0;
    }

    public static void main(String[] args) {
        int[] nums = {0,1,1,1,0,1,1,0,1};
        System.out.println(longestSubarray(nums));
    }
}
