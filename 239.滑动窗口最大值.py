#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
# https://leetcode-cn.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (48.84%)
# Likes:    533
# Dislikes: 0
# Total Accepted:    72.6K
# Total Submissions: 148.2K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k
# 个数字。滑动窗口每次只向右移动一位。
#
# 返回滑动窗口中的最大值。
#
#
#
# 进阶：
#
# 你能在线性时间复杂度内解决此题吗？
#
#
#
# 示例:
#
# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7]
# 解释:
#
# ⁠ 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length
#
#
#

# @lc code=start
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []

        ans = []
        max_queue = deque()
        for i in range(k):
            while len(max_queue) > 0 and nums[i] > max_queue[-1]:
                max_queue.pop()
            max_queue.append(nums[i])

        ans.append(max_queue[0])

        for i in range(k, len(nums)):
            if nums[i - k] == max_queue[0]:
                max_queue.popleft()
            while len(max_queue) > 0 and nums[i] > max_queue[-1]:
                max_queue.pop()
            max_queue.append(nums[i])
            ans.append(max_queue[0])

        return ans


# @lc code=end

