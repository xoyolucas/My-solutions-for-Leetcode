#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#
# https://leetcode-cn.com/problems/largest-number/description/
#
# algorithms
# Medium (37.32%)
# Likes:    437
# Dislikes: 0
# Total Accepted:    47.6K
# Total Submissions: 126.9K
# Testcase Example:  '[10,2]'
#
# 给定一组非负整数 nums，重新排列它们每个数字的顺序（每个数字不可拆分）使之组成一个最大的整数。
#
# 注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
#
#
#
# 示例 1：
#
#
# 输入：nums = [10,2]
# 输出："210"
#
# 示例 2：
#
#
# 输入：nums = [3,30,34,5,9]
# 输出："9534330"
#
#
# 示例 3：
#
#
# 输入：nums = [1]
# 输出："1"
#
#
# 示例 4：
#
#
# 输入：nums = [10]
# 输出："10"
#
#
#
#
# 提示：
#
#
# 1
# 0
#
#
#

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(num1, num2):
            tmp1 = int(str(num1)+str(num2))
            tmp2 = int(str(num2)+str(num1))
            if tmp1 > tmp2:
                return -1
            elif tmp1 == tmp2:
                return 0
            else:
                return 1

        nums = sorted(nums, key=functools.cmp_to_key(compare))

        res = ''
        for num in nums:
            res += str(num)

        return res if res[0] != '0' else '0'

# @lc code=end
