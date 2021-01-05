#
# @lc app=leetcode.cn id=149 lang=python3
#
# [149] 直线上最多的点数
#
# https://leetcode-cn.com/problems/max-points-on-a-line/description/
#
# algorithms
# Hard (23.36%)
# Likes:    203
# Dislikes: 0
# Total Accepted:    18.5K
# Total Submissions: 78.8K
# Testcase Example:  '[[1,1],[2,2],[3,3]]'
#
# 给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。
#
# 示例 1:
#
# 输入: [[1,1],[2,2],[3,3]]
# 输出: 3
# 解释:
# ^
# |
# |        o
# |     o
# |  o  
# +------------->
# 0  1  2  3  4
#
#
# 示例 2:
#
# 输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# 输出: 4
# 解释:
# ^
# |
# |  o
# |     o        o
# |        o
# |  o        o
# +------------------->
# 0  1  2  3  4  5  6
#
#

# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def gcd(x, y):
            if y == 0:
                return x
            else:
                return gcd(y, x % y)

        n = len(points)
        if n==0 or n==1:
            return n
        
        res = 1
        for i in range(n - 1):
            # 点1
            x1, y1 = points[i][0], points[i][1]
            # 斜率
            slope = {}
            same = 0
            for j in range(i + 1, n):
                # 点2
                x2, y2 = points[j][0], points[j][1]
                # 重叠点
                if x1 == x2 and y1 == y2:
                    same += 1
                else:
                    dy, dx = y2 - y1, x2 - x1
                    # 求公约数
                    g = gcd(dy, dx)
                    if g != 0:
                        dy //= g
                        dx //= g
                    slope['%s/%s' % (dy, dx)] = slope.get('%s/%s' % (dy, dx), 1) + 1
    
            res = max(res, max(slope.values()) + same) if len(slope)>0 else max(res,1+same)
            same = 0

        return res
# @lc code=end
