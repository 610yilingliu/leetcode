#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
class TrieNode(object):
    def __init__(self):
        self.children_node = {}
        self.item = ''


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    # 在树中插入字符串
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children_node:
                node.children_node[c] = TrieNode()
            node = node.children_node[c]

        node.item = word

    # 查询树中是否存在字符串
    def search(self, word):
        node = self.root
        for w in word:
            if w not in node.children_node:
                return False
            node = node.children_node[w]
        return node.item == word

    # 查询树中是否有字符串的前缀
    def starts_with(self, word):
        node = self.root
        for w in word:
            if w not in node.children_node:
                return False
            node = node.children_node[w]

        return True
        
class Solution(object):
    
        def findWords(self, board, words):
            result = []
            trie_node = Trie()
            # 构造前缀树
            for w in words:
                trie_node.insert(w)

            if not board and not board[0]:
                return

            exist_matrix = []
            for i in board:
                exist_matrix.append([False] * len(i))

            def find_word(row, col, s):
                if (row < 0 or row >= len(board)) or (col < 0 or col >= len(board[row])) or exist_matrix[row][col]:
                    return
            
                s += board[row][col]
                # 前缀查询字符串
                if not trie_node.starts_with(s):
                    return
                
                # 判断字符串是否在前缀树中
                if trie_node.search(s):
                    result.append(s)
                
                exist_matrix[row][col] = True
                find_word(row - 1, col, s)
                find_word(row + 1, col, s)
                find_word(row, col - 1, s)
                find_word(row, col + 1, s)
                exist_matrix[row][col] = False

            for i in range(len(board)):
                for j in range(len(board[i])):
                    find_word(i, j, "")

            return list(set(result))
# @lc code=end

