#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#
# https://leetcode-cn.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (51.23%)
# Likes:    482
# Dislikes: 0
# Total Accepted:    94.8K
# Total Submissions: 185.1K
# Testcase Example:  '"25525511135"'
#
# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
#
# 有效的 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
#
# 例如："0.1.2.201" 和 "192.168.1.1" 是 有效的 IP 地址，但是 "0.011.255.245"、"192.168.1.312"
# 和 "192.168@1.1" 是 无效的 IP 地址。
#
#
#
# 示例 1：
#
# 输入：s = "25525511135"
# 输出：["255.255.11.135","255.255.111.35"]
#
#
# 示例 2：
#
# 输入：s = "0000"
# 输出：["0.0.0.0"]
#
#
# 示例 3：
#
# 输入：s = "1111"
# 输出：["1.1.1.1"]
#
#
# 示例 4：
#
# 输入：s = "010010"
# 输出：["0.10.0.10","0.100.1.0"]
#
#
# 示例 5：
#
# 输入：s = "101023"
# 输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
#
#
#
#
# 提示：
#
#
# 0 <= s.length <= 3000
# s 仅由数字组成
#
#
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backTrace(index, element):
            # 终止条件
            if len(element) == 4:
                if index == len(s):
                    res.append('.'.join(element))
                return

            for i in range(1, 1+min(3, len(s)-index)):
                # 0**字符不符合规则
                if i != 1 and s[index] == '0':
                    break

                # 回溯
                if 0 <= int(s[index:index+i]) <= 255:
                    element.append(s[index:index+i])
                    backTrace(index+i, element)
                    element.pop()

        res = []
        backTrace(0, [])

        return res
# @lc code=end
