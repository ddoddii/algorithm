/*
 * @lc app=leetcode id=1219 lang=cpp
 *
 * [1219] Path with Maximum Gold
 */

// @lc code=start
#include <iostream>
#include <vector>
using namespace std;

class Solution
{
  public:
    vector<int> dxs = {1, 0, -1, 0};
    vector<int> dys = {0, -1, 0, 1};
    bool in_range(int x, int y, int row, int col)
    {
        return 0 <= x && x < row && 0 <= y && y < col;
    }

    int backtrack(int x, int y, int row, int col, vector<vector<int>> &grid, vector<vector<int>> &visited)
    {
        if (!(in_range(x, y, row, col)) || grid[x][y] == 0 || visited[x][y])
        {
            return 0;
        }
        visited[x][y] = 1;
        int maxGold = grid[x][y];
        for (int i = 0; i < 4; i++)
        {
            int nx = x + dxs[i];
            int ny = y + dys[i];
            maxGold = max(maxGold, grid[x][y] + backtrack(nx, ny, row, col, grid, visited));
        }
        visited[x][y] = 0;
        return maxGold;
    }

    int getMaximumGold(vector<vector<int>> &grid)
    {

        int row = grid.size(), col = grid[0].size();
        int maxGold = 0;
        vector<vector<int>> visited(row, vector<int>(col, 0));
        for (int i = 0; i < row; i++)
        {
            for (int j = 0; j < col; j++)
            {
                if (grid[i][j])
                {
                    maxGold = max(maxGold, backtrack(i, j, row, col, grid, visited));
                }
            }
        }
        return maxGold;
    }
};

int main()
{
    Solution solution;
    vector<vector<int>> grid = {{1, 0, 7}, {2, 0, 6}, {3, 4, 5}, {0, 3, 0}, {9, 0, 20}};
    cout << "Maximum gold collected: " << solution.getMaximumGold(grid) << endl;
    return 0;
}
// @lc code=end
