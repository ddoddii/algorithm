package leetcode;

//724. Find Pivot Index
public class P724 {
    public static int pivotIndex(int[] nums) {
        int sum = 0;
        for (int num : nums){
            sum += num;
        }
        int left = 0;
        int right = 0;
        for (int i = 0 ; i < nums.length ; i++){
            if ( i == 0){
                left = 0;
                right = sum - nums[i];
            }
            else{
                left += nums[i-1];
                right = sum - nums[i] - left;
            }
            if (left == right){
                return i;
            }

        }
        return -1;

    }

    public static void main(String[] args) {
        int[] nums = {1,7,3,6,5,6};
        System.out.println(pivotIndex(nums));

    }
}
