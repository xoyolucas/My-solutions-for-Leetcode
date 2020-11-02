#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] 常数时间插入、删除和获取随机元素
#
# https://leetcode-cn.com/problems/insert-delete-getrandom-o1/description/
#
# algorithms
# Medium (49.18%)
# Likes:    224
# Dislikes: 0
# Total Accepted:    18.8K
# Total Submissions: 38.3K
# Testcase Example:  '["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]\n' +
  '[[],[1],[2],[2],[],[1],[2],[]]'
#
# 设计一个支持在平均 时间复杂度 O(1) 下，执行以下操作的数据结构。
# 
# 
# insert(val)：当元素 val 不存在时，向集合中插入该项。
# remove(val)：元素 val 存在时，从集合中移除该项。
# getRandom：随机返回现有集合中的一项。每个元素应该有相同的概率被返回。
# 
# 
# 示例 :
# 
# 
# // 初始化一个空的集合。
# RandomizedSet randomSet = new RandomizedSet();
# 
# // 向集合中插入 1 。返回 true 表示 1 被成功地插入。
# randomSet.insert(1);
# 
# // 返回 false ，表示集合中不存在 2 。
# randomSet.remove(2);
# 
# // 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
# randomSet.insert(2);
# 
# // getRandom 应随机返回 1 或 2 。
# randomSet.getRandom();
# 
# // 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
# randomSet.remove(1);
# 
# // 2 已在集合中，所以返回 false 。
# randomSet.insert(2);
# 
# // 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。
# randomSet.getRandom();
# 
# 
#

# @lc code=start
import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict={}
        self.vec=[]

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict:
            return False
        
        self.dict[val]=len(self.vec)
        self.vec.append(val)
        return True


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            last=self.vec[-1]
            index=self.dict[val]
            self.vec[index]=last
            self.dict[last]=index

            self.vec.pop()
            del self.dict[val]
            return True
        else:
            return False


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.vec)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

