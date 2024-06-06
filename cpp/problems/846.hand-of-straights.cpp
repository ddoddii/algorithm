/*
 * @lc app=leetcode id=846 lang=cpp
 *
 * [846] Hand of Straights
 */

// @lc code=start
#include <iostream>
#include <map>
#include <vector>
using namespace std;

class Solution
{
  public:
    bool isNStraightHand(vector<int> &hand, int groupSize)
    {
        if (hand.size() % groupSize)
        {
            return false;
        }

        map<int, int> cardCount;
        for (int card : hand)
        {
            cardCount[card]++;
        }

        for (auto it = cardCount.begin(); it != cardCount.end(); ++it)
        {
            if (it->second > 0)
            {
                int count = it->second;
                for (int i = 0; i < groupSize; i++)
                {
                    if (cardCount[it->first + i] < count)
                    {
                        return false;
                    }
                    cardCount[it->first + i] -= count;
                }
            }
        }
        return true;
    }
};

int main()
{
    Solution solution;
    vector<int> hand = {1, 2, 3, 6, 2, 3, 4, 7, 8};
    int groupSize = 4;
    cout << "Result : " << solution.isNStraightHand(hand, groupSize) << endl;
    return 0;
}
// @lc code=end
