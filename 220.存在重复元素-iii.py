#
# @lc app=leetcode.cn id=220 lang=python3
#
# [220] 存在重复元素 III
#
# https://leetcode-cn.com/problems/contains-duplicate-iii/description/
#
# algorithms
# Medium (26.53%)
# Likes:    285
# Dislikes: 0
# Total Accepted:    29.1K
# Total Submissions: 109.6K
# Testcase Example:  '[1,2,3,1]\n3\n0'
#
# 在整数数组 nums 中，是否存在两个下标 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值小于等于 t ，且满足 i 和 j
# 的差的绝对值也小于等于 ķ 。
#
# 如果存在则返回 true，不存在返回 false。
#
#
#
# 示例 1:
#
# 输入: nums = [1,2,3,1], k = 3, t = 0
# 输出: true
#
# 示例 2:
#
# 输入: nums = [1,0,1,1], k = 1, t = 2
# 输出: true
#
# 示例 3:
#
# 输入: nums = [1,5,9,1,5,9], k = 2, t = 3
# 输出: false
#
#

# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        def getID(x, size):
            return x//size

        if k <= 0 or t < 0:
            return False

        bucket = {}
        for i in range(len(nums)):
            key = nums[i]//(t+1)
            # 桶里只需要包含最多一个元素就可以了，因为如果任意一个桶中包含了两个元素，那么这也就是意味着这两个元素是足够接近
            if key in bucket.keys():
                return True
            if key-1 in bucket.keys() and abs(nums[i]-bucket[key-1]) <= t:
                return True
            if key+1 in bucket.keys() and abs(nums[i]-bucket[key+1]) <= t:
                return True
            bucket[key] = nums[i]

            if i >= k:
                bucket.pop(nums[i-k]//(t+1))

        return False

# @lc code=end

# public class Solution {
#     // Get the ID of the bucket from element value x and bucket width w
#     // In Java, `-3 / 5 = 0` and but we need `-3 / 5 = -1`.
#     private long getID(long x, long w) {
#         return x < 0 ? (x + 1) / w - 1 : x / w;
#     }

#     public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
#         if (t < 0) return false;
#         Map<Long, Long> d = new HashMap<>();
#         long w = (long)t + 1;
#         for (int i = 0; i < nums.length; ++i) {
#             long m = getID(nums[i], w);
#             // check if bucket m is empty, each bucket may contain at most one element
#             if (d.containsKey(m))
#                 return true;
#             // check the nei***or buckets for almost duplicate
#             if (d.containsKey(m - 1) && Math.abs(nums[i] - d.get(m - 1)) < w)
#                 return true;
#             if (d.containsKey(m + 1) && Math.abs(nums[i] - d.get(m + 1)) < w)
#                 return true;
#             // now bucket m is empty and no almost duplicate in nei***or buckets
#             d.put(m, (long)nums[i]);
#             if (i >= k) d.remove(getID(nums[i - k], w));
#         }
#         return false;
#     }
# }
