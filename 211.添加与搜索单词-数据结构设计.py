#
# @lc app=leetcode.cn id=211 lang=python3
#
# [211] 添加与搜索单词 - 数据结构设计
#
# https://leetcode-cn.com/problems/design-add-and-search-words-data-structure/description/
#
# algorithms
# Medium (47.05%)
# Likes:    202
# Dislikes: 0
# Total Accepted:    19.4K
# Total Submissions: 41.3K
# Testcase Example:  '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
#
# 请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。
#
# 实现词典类 WordDictionary ：
#
#
# WordDictionary() 初始化词典对象
# void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配
# bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；否则，返回  false 。word 中可能包含一些
# '.' ，每个 . 都可以表示任何一个字母。
#
#
#
#
# 示例：
#
#
# 输入：
#
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# 输出：
# [null,null,null,null,false,true,true,true]
#
# 解释：
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
#
#
#
#
# 提示：
#
#
# 1
# addWord 中的 word 由小写英文字母组成
# search 中的 word 由 '.' 或小写英文字母组成
# 最调用多 50000 次 addWord 和 search
#
#
#

# @lc code=start
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char in node.keys():
                node = node[char]
            else:
                node[char] = {}
                node = node[char]
        node['end'] = True

    def search(self, word: str) -> bool:
        def backtrace(word, node):
            for i in range(len(word)):
                # 通配符进行查找，回溯
                if word[i] == '.':
                    for x in [chr(x) for x in range(ord('a'), ord('z') + 1)]:
                        if x in node.keys() and backtrace(x+word[i+1:], node):
                            return True
                    return False
                # 包含该字母
                if word[i] in node.keys():
                    node = node[word[i]]
                # 不包含该字母
                else:
                    return False
            # 判断是否有结束标志
            return 'end' in node.keys()

        return backtrace(word, self.root)
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
