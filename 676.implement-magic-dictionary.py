#
# @lc app=leetcode id=676 lang=python3
#
# [676] Implement Magic Dictionary
#

# @lc code=start
import collections

class MagicDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = dict()
        self.wordlength = collections.defaultdict(set)
    

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        """
        for word in dict:
            self.wordlength[len(word)].add(word)

    def search(self, word: str):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        if not word:
            return False
        if len(word) not in self.wordlength:
            return False
        waitinglist = self.wordlength[len(word)]
        def isvalid(word1, word2):
            if word1 == word2:
                return False
            s = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    s += 1
                if s > 1:
                    return False
            return True

        for w in waitinglist:
            if isvalid(w, word):
                return True
        return False


                    



# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(["a","b","ab","abc","abcabacbababdbadbfaejfoiawfjaojfaojefaowjfoawjfoawj","abcdefghijawefe","aefawoifjowajfowafjeoawjfaow","cba","cas","aaewfawi","babcda","bcd","awefj"])
# param_2 = obj.search("cbc")
# print(param_2)
# @lc code=end

