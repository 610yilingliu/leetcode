#
# @lc app=leetcode id=1032 lang=python3
#
# [1032] Stream of Characters
#
# @lc code=start
class StreamChecker:
    # Trie version
    def __init__(self, words: List[str]):
        self.Trie={}
        for word in words:
            curnode=self.Trie
            word=word[::-1]
            for ch in word:
                if ch not in curnode:
                    curnode[ch]={}
                curnode=curnode[ch]
            curnode['#']=1 # '#' means the end of a word
        self.pre=''
 
    def query(self, letter: str) -> bool:
        self.pre=self.pre+letter
        curnode=self.Trie
        for i in range(0,len(self.pre)):
            if self.pre[-i-1] not in curnode:
                break
            curnode=curnode[self.pre[-i-1]]
            if '#' in curnode:
                return True
        return False
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
# @lc code=end

