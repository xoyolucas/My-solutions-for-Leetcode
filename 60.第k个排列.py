#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
#
# https://leetcode-cn.com/problems/permutation-sequence/description/
#
# algorithms
# Medium (48.41%)
# Likes:    204
# Dislikes: 0
# Total Accepted:    27.7K
# Total Submissions: 57.1K
# Testcase Example:  '3\n3'
#
# 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
# 
# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
# 
# 
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 
# 
# 给定 n 和 k，返回第 k 个排列。
# 
# 说明：
# 
# 
# 给定 n 的范围是 [1, 9]。
# 给定 k 的范围是[1,  n!]。
# 
# 
# 示例 1:
# 
# 输入: n = 3, k = 3
# 输出: "213"
# 
# 
# 示例 2:
# 
# 输入: n = 4, k = 9
# 输出: "2314"
# 
# 
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorials = [1]
        nums = ['1']

        for i in range(1, n):
            # 生成阶乘数排列 0!, 1!, ..., (n - 1)!
            factorials.append(factorials[i - 1] * i)
            # 生成原始数列['1','2'....'n']
            nums.append(str(i + 1))
        
        k -= 1
        
        # compute factorial representation of k
        output = []
        for i in range(n - 1, -1, -1):
            index = k // factorials[i] # 对应nums的位置
            k -= index * factorials[i]
            
            output.append(nums[index])
            del nums[index]
        
        return ''.join(output)

# @lc code=end

