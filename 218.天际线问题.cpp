/*
 * @lc app=leetcode.cn id=218 lang=cpp
 *
 * [218] 天际线问题
 *
 * https://leetcode-cn.com/problems/the-skyline-problem/description/
 *
 * algorithms
 * Hard (44.94%)
 * Likes:    318
 * Dislikes: 0
 * Total Accepted:    11.7K
 * Total Submissions: 26K
 * Testcase Example:  '[[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]'
 *
 * 城市的天际线是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。给你所有建筑物的位置和高度，请返回由这些建筑物形成的 天际线 。
 * 
 * 每个建筑物的几何信息由数组 buildings 表示，其中三元组 buildings[i] = [lefti, righti, heighti]
 * 表示：
 * 
 * 
 * lefti 是第 i 座建筑物左边缘的 x 坐标。
 * righti 是第 i 座建筑物右边缘的 x 坐标。
 * heighti 是第 i 座建筑物的高度。
 * 
 * 
 * 天际线 应该表示为由 “关键点” 组成的列表，格式 [[x1,y1],[x2,y2],...] ，并按 x 坐标 进行 排序
 * 。关键点是水平线段的左端点。列表中最后一个点是最右侧建筑物的终点，y 坐标始终为 0
 * ，仅用于标记天际线的终点。此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。
 * 
 * 注意：输出天际线中不得有连续的相同高度的水平线。例如 [...[2 3], [4 5], [7 5], [11 5], [12 7]...]
 * 是不正确的答案；三条高度为 5 的线应该在最终输出中合并为一个：[...[2 3], [4 5], [12 7], ...]
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
 * 输出：[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
 * 解释：
 * 图 A 显示输入的所有建筑物的位置和高度，
 * 图 B 显示由这些建筑物形成的天际线。图 B 中的红点表示输出列表中的关键点。
 * 
 * 示例 2：
 * 
 * 
 * 输入：buildings = [[0,2,3],[2,5,3]]
 * 输出：[[0,3],[5,0]]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 
 * 0 i < righti 
 * 1 i 
 * buildings 按 lefti 非递减排序
 * 
 * 
 */

// @lc code=start
#include <vector>
#include <set>
using namespace std;

class Solution
{
public:
    //使用扫描线，从左至右扫过。如果遇到左端点，将高度入堆，如果遇到右端点，则将高度从堆中删除。
    //使用 last 变量记录上一个转折点。
    vector<vector<int>> getSkyline(vector<vector<int>> &buildings)
    {
        vector<vector<int>> res;
        multiset<pair<int, int>> skylines;

        for (auto &building : buildings)
        {
            //左边界
            skylines.insert(make_pair(building[0], -building[2]));
            //右边界
            skylines.insert(make_pair(building[1], building[2]));
        }

        // 保存当前位置所有高度。
        multiset<int> heights({0});
        // 保存上一个位置的横坐标以及高度
        vector<int> last{0, 0};

        for (auto &x : skylines)
        {
            // 左边界，高度入堆
            if (x.second < 0)
            {
                heights.insert(-x.second);
            }
            // 右边界，移除
            else
            {
                heights.erase(heights.find(x.second));
            }

            int max_height = *heights.rbegin();
            if (last[1] != max_height)
            {
                last[0] = x.first;
                last[1] = max_height;
                res.emplace_back(last);
            }
        }

        return res;
    }
};
// @lc code=end
