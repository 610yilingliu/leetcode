#
# @lc app=leetcode id=211 lang=python3
#
# [211] Add and Search Word - Data structure design
#
import collections
# @lc code=start
class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.is_word = False
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def addWord(self, word: str):
        """
        Adds a word into the data structure.
        """
        cur = self.root
        for char in word:
            cur = cur.children[char]
        cur.is_word = True

    def search(self, word: str):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        return self.matcher(word, 0, self.root)

    def matcher(self, word, idx, root):
        if root == None:
            return False
        if idx == len(word):
            return root.is_word
        if word[idx] != '.':
            return self.matcher(word, idx + 1, root.children.get(word[idx]))
        else:
            for child in root.children.values():
                if self.matcher(word, idx + 1, child):
                    return True
            return False
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

