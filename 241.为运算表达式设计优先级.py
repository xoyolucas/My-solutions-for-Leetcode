#
# @lc app=leetcode.cn id=241 lang=python3
#
# [241] 为运算表达式设计优先级
#
# https://leetcode-cn.com/problems/different-ways-to-add-parentheses/description/
#
# algorithms
# Medium (73.08%)
# Likes:    320
# Dislikes: 0
# Total Accepted:    19.8K
# Total Submissions: 27.2K
# Testcase Example:  '"2-1-1"'
#
# 给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及
# * 。
# 
# 示例 1:
# 
# 输入: "2-1-1"
# 输出: [0, 2]
# 解释: 
# ((2-1)-1) = 0 
# (2-(1-1)) = 2
# 
# 示例 2:
# 
# 输入: "2*3-4*5"
# 输出: [-34, -14, -10, -10, 10]
# 解释: 
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10
# 
#

# @lc code=start

# 分治算法三步走：
# 分解：按运算符分成左右两部分，分别求解
# 解决：实现一个递归函数，输入算式，返回算式解
# 合并：根据运算符合并左右两部分的解，得出最终解
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit():
            return [int(input)]
        
        res=[]
        for i,char in enumerate(input):
            if char in ['+','-','*']:
                # 左右两侧分治
                nums1=self.diffWaysToCompute(input[:i])
                nums2=self.diffWaysToCompute(input[i+1:])
                
                for num1 in nums1:
                    for num2 in nums2:
                        if char=='+':
                            res.append(num1+num2)
                        elif char=='-':
                            res.append(num1-num2)
                        elif char=='*':
                            res.append(num1*num2)
                
        return res   
# @lc code=end

