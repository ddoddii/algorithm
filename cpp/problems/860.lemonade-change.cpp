/*
 * @lc app=leetcode id=860 lang=cpp
 *
 * [860] Lemonade Change
 */

// @lc code=start
#include <iostream>
#include <vector>
using namespace std;

class Solution
{
  public:
    bool lemonadeChange(vector<int> &bills)
    {
        int five_dollar = 0;
        int ten_dollar = 0;
        int n = bills.size();
        for (int i = 0; i < n; i++)
        {
            if (bills[i] == 5)
            {
                five_dollar++;
            }
            else if (bills[i] == 10)
            {
                if (five_dollar > 0)
                    five_dollar--;
                else
                    return false;
                ten_dollar++;
            }
            else
            {
                if (five_dollar > 0 && ten_dollar > 0)
                {
                    five_dollar--;
                    ten_dollar--;
                }
                else if (five_dollar > 2)
                {
                    five_dollar -= 3;
                }
                else
                    return false;
            }
        }
    }
};
// @lc code=end
