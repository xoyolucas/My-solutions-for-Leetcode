#
# @lc app=leetcode.cn id=187 lang=python3
#
# [187] 重复的DNA序列
#
# https://leetcode-cn.com/problems/repeated-dna-sequences/description/
#
# algorithms
# Medium (46.24%)
# Likes:    140
# Dislikes: 0
# Total Accepted:    27.7K
# Total Submissions: 60K
# Testcase Example:  '"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"'
#
# 所有 DNA 都由一系列缩写为 'A'，'C'，'G' 和 'T' 的核苷酸组成，例如："ACGAATTCCG"。在研究 DNA 时，识别 DNA
# 中的重复序列有时会对研究非常有帮助。
#
# 编写一个函数来找出所有目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。
#
#
#
# 示例 1：
#
#
# 输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# 输出：["AAAAACCCCC","CCCCCAAAAA"]
#
#
# 示例 2：
#
#
# 输入：s = "AAAAAAAAAAAAA"
# 输出：["AAAAAAAAAA"]
#
#
#
#
# 提示：
#
#
# 0
# s[i] 为 'A'、'C'、'G' 或 'T'
#
#
#

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n <= 10:
            return []

        to_bits = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        nums = [to_bits[s[i]] for i in range(n)]

        visited = set()
        res = set()

        for start in range(n-9):
            mask = 0
            for i in range(10):
                mask <<= 2
                mask |= nums[start+i]

            if mask in visited:
                res.add(s[start:start+10])
            else:
                visited.add(mask)

        return list(res)

# @lc code=end


# class Solution:
#     def findRepeatedDnaSequences(self, s: str) -> List[str]:
#         L, n = 10, len(s)
#         if n <= L:
#             return []

#         # convert string to the array of 2-bits integers:
#         # 00_2, 01_2, 10_2 or 11_2
#         to_int = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
#         nums = [to_int.get(s[i]) for i in range(n)]

#         bitmask = 0
#         seen, output = set(), set()
#         # iterate over all sequences of length L
#         for start in range(n - L + 1):
#             # compute bitmask of the sequence in O(1) time
#             if start != 0:
#                 # left shift to free the last 2 bit
#                 bitmask <<= 2
#                 # add a new 2-bits number in the last two bits
#                 bitmask |= nums[start + L - 1]
#                 # unset first two bits: 2L-bit and (2L + 1)-bit
#                 bitmask &= ~(3 << 2 * L)
#             # compute bitmask of the first sequence in O(L) time
#             else:
#                 for i in range(L):
#                     bitmask <<= 2
#                     bitmask |= nums[i]
#             if bitmask in seen:
#                 output.add(s[start:start + L])
#             seen.add(bitmask)
#         return output
