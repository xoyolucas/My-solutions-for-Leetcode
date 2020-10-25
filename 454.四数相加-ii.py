#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#
# https://leetcode-cn.com/problems/4sum-ii/description/
#
# algorithms
# Medium (56.38%)
# Likes:    215
# Dislikes: 0
# Total Accepted:    29.3K
# Total Submissions: 51.9K
# Testcase Example:  '[1,2]\n[-2,-1]\n[-1,2]\n[0,2]'
#
# 给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] +
# D[l] = 0。
#
# 为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -2^28 到 2^28 - 1
# 之间，最终结果不会超过 2^31 - 1 。
#
# 例如:
#
#
# 输入:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
#
# 输出:
# 2
#
# 解释:
# 两个元组如下:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
#
#
#

# @lc code=start
class Solution:
    def fourSumCount(
        self, A: List[int], B: List[int], C: List[int], D: List[int]
    ) -> int:
        res = 0
        AplusB = {}

        for a in A:
            for b in B:
                sum1 = a + b
                AplusB[sum1] = AplusB.get(sum1, 0) + 1

        for c in C:
            for d in D:
                sum2 = c + d
                if -sum2 in AplusB.keys():
                    res += AplusB[-sum2]

        return res


# @lc code=end

