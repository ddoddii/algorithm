/*
 * @lc app=leetcode id=1863 lang=java
 *
 * [1863] Sum of All Subset XOR Totals
 */

// @lc code=start
public class P1863{
    class Solution {
        public int subsetXORSum(int[] nums) {
            return helper(nums,0,0);
        }
    
        private int helper(int[] nums, int i, int currXor) {
            if (i == nums.length) {
                return currXor;
            }
            int include = helper(nums,i+1,currXor^nums[i]);
            int exclude = helper(nums,i+1,currXor);
            return include + exclude;
        }
    }

    public static void main(String[] args) {
        P1863 instance = new P1863();
        Solution solution = instance.new Solution();
        int[] nums = {1,3};
        int result = solution.subsetXORSum(nums);
        System.out.println(result); 
    }
}



// @lc code=end

