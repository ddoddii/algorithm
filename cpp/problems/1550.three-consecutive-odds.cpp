/*
 * @lc app=leetcode id=1550 lang=cpp
 *
 * [1550] Three Consecutive Odds
 */

// @lc code=start
#include <iostream>
#include <vector>
using namespace std;

class Solution
{
  public:
    bool threeConsecutiveOdds(vector<int> &arr)
    {
        int odds = 0;
        for (auto i = 0; i < arr.size() && odds < 3; ++i)
        {
            odds = arr[i] % 2 ? odds + 1 : 0;
        }
        return odds == 3;
    }
};
// @lc code=end
