#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#
# https://leetcode-cn.com/problems/lru-cache/description/
#
# algorithms
# Medium (50.59%)
# Likes:    856
# Dislikes: 0
# Total Accepted:    97.1K
# Total Submissions: 191.7K
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' + '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
#
# 获取数据 get(key) - 如果关键字 (key) 存在于缓存中，则获取关键字的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) -
# 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字/值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
#
#
#
# 进阶:
#
# 你是否可以在 O(1) 时间复杂度内完成这两种操作？
#
#
#
# 示例:
#
# LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // 返回  1
# cache.put(3, 3);    // 该操作会使得关键字 2 作废
# cache.get(2);       // 返回 -1 (未找到)
# cache.put(4, 4);    // 该操作会使得关键字 1 作废
# cache.get(1);       // 返回 -1 (未找到)
# cache.get(3);       // 返回  3
# cache.get(4);       // 返回  4
#
#
#

# @lc code=start
class LinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        # 双向链表
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = dict()
        self.head = LinkedNode()
        self.tail = LinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def addHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def move2head(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.addHead(node)

    def removeTail(self):
        node = self.tail.prev
        node.prev.next = node.next
        node.next.prev = node.prev
        return node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.move2head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        # 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.move2head(node)
        # 如果 key 不存在，创建一个新的节点
        else:
            node = LinkedNode(key, value)
            self.cache[key] = node
            self.size += 1
            self.addHead(node)

            if self.size > self.capacity:
                self.size -= 1
                remove = self.removeTail()
                self.cache.pop(remove.key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

