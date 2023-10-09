package leetcode;

import java.util.Arrays;

// 238. Product of Array Except self
public class p238 {

    //Time Limit
    public static int[] productExceptSelf(int[] nums) {

        int[] answer = new int[nums.length];
        for (int i = 0 ; i < nums.length ; i++){
            int calLeft = 1 ;
            int calRight = 1;
            for (int j = 0 ; j < i ; j++){
                calLeft = calLeft * nums[j];
            }
            for (int k = nums.length -1  ; k > i ; k--){
                calRight = calRight * nums[k];
            }
            answer[i] = calLeft * calRight;
        }
        return answer;

    }

    public static int[] productExceptSelf2(int[] nums) {
        int[] answer = new int[nums.length];
        int productWithoutZero = 1;
        boolean hasZero = false;
        int numZeros = 0;
        for (int i = 0 ; i < nums.length ; i++){
            if (nums[i] != 0){
                productWithoutZero *= nums[i];

            }
            else{
                hasZero = true;
                numZeros++;
            }
        }
        for (int i = 0 ; i < nums.length ; i++){
            if (!hasZero){
                answer[i] = productWithoutZero / nums[i];
            }
            else{
                if (numZeros > 1){
                    answer[i] = 0;
                }
                else if (numZeros == 1){
                    if (nums[i] != 0 ){
                        answer[i] = 0;
                    }
                    else{
                        answer[i] = productWithoutZero;
                    }
                }
            }
        }
        return answer;
    }

    //Time Limit
    public static int[] productExceptSelf3(int[] nums) {
        int n = nums.length;
        int[] answer = new int[n];

        for (int i = 0 ; i < n ; i++){
            int pro = 1;
            for (int j = 0 ; j < n ; j++){
                if (i == j) continue;
                pro *= nums[j];
            }
            answer[i] = pro;
        }
        return answer;
    }

    //TODO : 다시보기
    public static int[] productExceptSelf4(int[] nums) {
        int n = nums.length;
        int[] answer = new int[n];
        Arrays.fill(answer,1);
        int curr = 1;

        for (int i = 0; i< n ; i++){
            answer[i] *= curr;
            curr *= nums[i];
        }
        curr = 1;
        for (int i = n-1 ; i >= 0; i--){
            answer[i] *= curr;
            curr *= nums[i];
        }
        return answer;

    }


    public static void main(String[] args) {
        int[] nums = {0,4,0};
        int[] answer = productExceptSelf3(nums);
        for (int i = 0 ; i < answer.length; i++){
            System.out.println(answer[i]);
        }


    }
}
