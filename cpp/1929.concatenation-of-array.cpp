/*
 * @lc app=leetcode id=1929 lang=cpp
 *
 * [1929] Concatenation of Array
 */

// @lc code=start
#include <iostream>
#include <vector>

class Solution
{
  public:
    std::vector<int> getConcatenation(std::vector<int> &nums)
    {
        size_t size = nums.size();
        int doubleSize = size * 2;
        std::vector<int> res(doubleSize);
        for (size_t i = 0; i < res.size(); ++i)
        {
            res[i] = nums[i % size];
        }
        return res;
    }
};

int main()
{
    std::vector<int> nums = {1, 2, 3};

    Solution sol;

    std::vector<int> result = sol.getConcatenation(nums);

    std::copy(result.begin(), result.end(), std::ostream_iterator<int>(std::cout, " "));
    std::cout << std::endl;

    return 0;
}

// @lc code=end
