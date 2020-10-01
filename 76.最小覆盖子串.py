#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
# https://leetcode-cn.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (39.23%)
# Likes:    772
# Dislikes: 0
# Total Accepted:    81.2K
# Total Submissions: 207.1K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# 给你一个字符串 S、一个字符串 T 。请你设计一种算法，可以在 O(n) 的时间复杂度内，从字符串 S 里面找出：包含 T 所有字符的最小子串。
#
#
#
# 示例：
#
# 输入：S = "ADOBECODEBANC", T = "ABC"
# 输出："BANC"
#
#
#
# 提示：
#
#
# 如果 S 中不存这样的子串，则返回空字符串 ""。
# 如果 S 中存在这样的子串，我们保证它是唯一的答案。
#
#
#

# @lc code=start


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = len(t)
        need = dict()
        for c in t:
            need[c] = need.get(c, 0)+1

        ans = ''
        left = 0
        for right, c in enumerate(s):
            if need.get(c, 0) > 0:
                count -= 1
            need[c] = need.get(c, 0)-1

            # 满足子串要求
            if count == 0:
                while True:
                    # 缩小左边界
                    if need[s[left]] == 0:
                        break
                    need[s[left]] += 1
                    left += 1

                size = len(ans)
                if size == 0 or size > right-left+1:
                    ans = s[left:right+1]

                # 缩小左边界直至不满足子串约束，标记缺少的字符
                need[s[left]] += 1
                left += 1
                count += 1

        return ans
# @lc code=end
