package leetcode;


// 1004. Max Consecutive Ones III
public class P1004 {
    public static int longestOnes(int[] nums, int k) {
        int left = 0;
        int right = 0;
        int zeroCount = 0;
        int max = 0;
        while (right < nums.length){
            if (nums[right] == 0){
                zeroCount++;
            }
            while(zeroCount > k){
                if (nums[left] == 0){
                    zeroCount--;
                }
                left++;
            }
            max = Math.max(max, right-left+1);
            right++;

        }

        return max;
    }

    public static void main(String[] args) {
        int[] nums = {0,0,1,1,0,1};
        int k = 2;
        System.out.println(longestOnes(nums,k));


    }

}
