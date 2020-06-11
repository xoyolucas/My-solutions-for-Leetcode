#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#
# https://leetcode-cn.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (67.78%)
# Likes:    300
# Dislikes: 0
# Total Accepted:    33.7K
# Total Submissions: 49.7K
# Testcase Example:  '"aab"'
#
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
#
# 返回 s 所有可能的分割方案。
#
# 示例:
#
# 输入: "aab"
# 输出:
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
#
#

# @lc code=start


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 0:
            return [[]]
        elif len(s) == 1:
            return [[s]]

        result = []
        for i in range(1, len(s)+1):
            left = s[:i]
            # 左侧是否为回文数
            if left != left[::-1]:
                continue
            else:
                right = s[i:]
                right_res = self.partition(right)
                # 左边的回文数+右边的回文数组合
                for right_element in right_res:
                    result.append([left] + right_element)

        return result


# @lc code=end