/*
 * @lc app=leetcode.cn id=874 lang=cpp
 *
 * [874] 模拟行走机器人
 *
 * https://leetcode-cn.com/problems/walking-robot-simulation/description/
 *
 * algorithms
 * Easy (31.50%)
 * Likes:    67
 * Dislikes: 0
 * Total Accepted:    5.4K
 * Total Submissions: 16.9K
 * Testcase Example:  '[4,-1,3]\n[]'
 *
 * 机器人在一个无限大小的网格上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令：
 * 
 * 
 * -2：向左转 90 度
 * -1：向右转 90 度
 * 1 <= x <= 9：向前移动 x 个单位长度
 * 
 * 
 * 在网格上有一些格子被视为障碍物。
 * 
 * 第 i 个障碍物位于网格点  (obstacles[i][0], obstacles[i][1])
 * 
 * 如果机器人试图走到障碍物上方，那么它将停留在障碍物的前一个网格方块上，但仍然可以继续该路线的其余部分。
 * 
 * 返回从原点到机器人的最大欧式距离的平方。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入: commands = [4,-1,3], obstacles = []
 * 输出: 25
 * 解释: 机器人将会到达 (3, 4)
 * 
 * 
 * 示例 2：
 * 
 * 输入: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
 * 输出: 65
 * 解释: 机器人在左转走到 (1, 8) 之前将被困在 (1, 4) 处
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 0 <= commands.length <= 10000
 * 0 <= obstacles.length <= 10000
 * -30000 <= obstacle[i][0] <= 30000
 * -30000 <= obstacle[i][1] <= 30000
 * 答案保证小于 2 ^ 31
 * 
 * 
 */

// @lc code=start
#include <vector>
#include <set>
#include <algorithm>
#include <utility>
using namespace std;

class Solution
{
public:
    int robotSim(vector<int> &commands, vector<vector<int>> &obstacles)
    {
        // 四个方向
        int dx[4] = {0, 1, 0, -1};
        int dy[4] = {1, 0, -1, 0};

        int x = 0, y = 0, di = 0;

        set<pair<int, int>> obstacleSet;
        for (auto &obstacle : obstacles)
        {
            obstacleSet.insert(make_pair(obstacle[0], obstacle[1]));
        }

        int ans = 0;
        for (int cmd : commands)
        {
            if (cmd == -2)
            {
                di = (di + 3) % 4;
            }
            else if (cmd == -1)
            {

                di = (di + 1) % 4;
            }
            else
            {
                for (int k = 0; k < cmd; ++k)
                {
                    int tmpx = x + dx[di];
                    int tmpy = y + dy[di];
                    if (obstacleSet.find(make_pair(tmpx, tmpy)) == obstacleSet.end())
                    {
                        x = tmpx;
                        y = tmpy;
                        ans = max(ans, x * x + y * y);
                    }
                    else
                    {
                        break;
                    }
                    
                }
            }
        }
        return ans;
    }
};
// @lc code=end
