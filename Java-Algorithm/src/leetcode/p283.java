package leetcode;

// 283. Move Zeros
public class p283 {

    // swap (Quicksort) 기억하기
    public static void main(String[] args) {
        int[] nums = {1,0,2,0,3,0,1,0,0,0,1};
        int left = 0 ;
        int right = 1;
        while(right < nums.length){

            if (nums[left] == 0 && nums[right] != 0){
                int temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
                left++;
                right++;
            }
            else if (right == nums.length -1) {
                left++;
                right = left + 1;
            }
            else {
                right++;
            }
        }

        for (int num : nums){
            System.out.println(num);
        }
    }
}
