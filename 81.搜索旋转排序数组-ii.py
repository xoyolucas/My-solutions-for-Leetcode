#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#
# https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/description/
#
# algorithms
# Medium (36.35%)
# Likes:    270
# Dislikes: 0
# Total Accepted:    49.6K
# Total Submissions: 136.3K
# Testcase Example:  '[2,5,6,0,0,1,2]\n0'
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。
#
# 编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。
#
# 示例 1:
#
# 输入: nums = [2,5,6,0,0,1,2], target = 0
# 输出: true
#
#
# 示例 2:
#
# 输入: nums = [2,5,6,0,0,1,2], target = 3
# 输出: false
#
# 进阶:
#
#
# 这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
# 这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？
#
#
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = left+(right-left)//2
            if nums[mid] == target:
                return True

            # 左边是升序的
            if nums[left] < nums[mid]:
                if target < nums[mid] and target >= nums[left]:
                    right = mid-1
                else:
                    left = mid+1
            # 中间点和最左边相等
            elif nums[left] == nums[mid]:
                while left <= right and nums[left] == nums[mid]:
                    left += 1
            # 右边是升序的
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1

        return False
# @lc code=end
