#
# @lc app=leetcode.cn id=260 lang=python3
#
# [260] 只出现一次的数字 III
#
# https://leetcode-cn.com/problems/single-number-iii/description/
#
# algorithms
# Medium (73.31%)
# Likes:    353
# Dislikes: 0
# Total Accepted:    36.3K
# Total Submissions: 49.5K
# Testcase Example:  '[1,2,1,3,2,5]'
#
# 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。
#
#
#
# 进阶：你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,2,1,3,2,5]
# 输出：[3,5]
# 解释：[5, 3] 也是有效的答案。
#
#
# 示例 2：
#
#
# 输入：nums = [-1,0]
# 输出：[-1,0]
#
#
# 示例 3：
#
#
# 输入：nums = [0,1]
# 输出：[1,0]
#
#
# 提示：
#
#
# 2
# -2^31
# 除两个只出现一次的整数外，nums 中的其他数字都出现两次
#
#
#

# @lc code=start

# 如果我们可以把所有数字分成两组，使得：
# 两个只出现一次的数字在不同的组中；
# 相同的数字会被分到相同的组中。
import functools


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # 所有元素异或的结果
        res = functools.reduce(lambda x, y: x ^ y, nums)

        # 找到res为1的那个位置，为1代表结果a和b在那一位不同，用来将所有数组分为两组
        div = 1
        while div & res == 0:
            div <<= 1

        # 分为两组后分别进行异或操作
        a, b = 0, 0
        for num in nums:
            if num & div == 0:
                a ^= num
            else:
                b ^= num

        return [a, b]

# @lc code=end
