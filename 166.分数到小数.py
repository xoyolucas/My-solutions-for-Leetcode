#
# @lc app=leetcode.cn id=166 lang=python3
#
# [166] 分数到小数
#
# https://leetcode-cn.com/problems/fraction-to-recurring-decimal/description/
#
# algorithms
# Medium (28.14%)
# Likes:    193
# Dislikes: 0
# Total Accepted:    18K
# Total Submissions: 63.8K
# Testcase Example:  '1\n2'
#
# 给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以 字符串形式返回小数 。
#
# 如果小数部分为循环小数，则将循环的部分括在括号内。
#
# 如果存在多个答案，只需返回 任意一个 。
#
# 对于所有给定的输入，保证 答案字符串的长度小于 10^4 。
#
#
#
# 示例 1：
#
#
# 输入：numerator = 1, denominator = 2
# 输出："0.5"
#
#
# 示例 2：
#
#
# 输入：numerator = 2, denominator = 1
# 输出："2"
#
#
# 示例 3：
#
#
# 输入：numerator = 2, denominator = 3
# 输出："0.(6)"
#
#
# 示例 4：
#
#
# 输入：numerator = 4, denominator = 333
# 输出："0.(012)"
#
#
# 示例 5：
#
#
# 输入：numerator = 1, denominator = 5
# 输出："0.2"
#
#
#
#
# 提示：
#
# -2^31 <= numerator, denominator <= 2^31 - 1
# denominator != 0
#
#
#

# @lc code=start
# 需要用一个哈希表记录余数出现在小数部分的位置，当发现已经出现的余数，就可以将重复出现的小数部分用括号括起来。
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'

        res = []
        # 异或，确定正负号
        if (numerator < 0) ^ (denominator < 0):
            res.append('-')

        # 取正整数
        numerator = abs(numerator)
        denominator = abs(denominator)

        num, remainder = divmod(numerator, denominator)
        res.append(str(num))
        # 无小数
        if remainder == 0:
            return ''.join(res)

        # 小数点
        res.append('.')

        index = {}
        while remainder != 0:
            # 出现重复的余数，即循环小数，跳出
            if remainder in index:
                res.insert(index[remainder], '(')
                res.append(')')
                break

            # 记录若循环小数，括号的位置
            index[remainder] = len(res)

            # 继续除法
            remainder *= 10
            num, remainder = divmod(remainder, denominator)
            res.append(str(num))

        return ''.join(res)

# @lc code=end
