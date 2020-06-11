#
# @lc app=leetcode id=408 lang=python3
#
# [408] Valid Word Abbreviation
#

# @lc code=start
import collections
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str):
        word = collections.deque(word)
        abbr = collections.deque(abbr)
        while word and abbr:
            if word[0] == abbr[0]:
                word.popleft()
                abbr.popleft()
            elif abbr[0].isnumeric():
                time = int(abbr.popleft())
                if time == 0:
                    return False
                while abbr and abbr[0].isnumeric():
                    time = time * 10 + int(abbr.popleft())
                for _ in range(time):
                    if word:
                        word.popleft()
                    else:
                        return False
            else:
                return False
        if word or abbr:
            return False
        return True

# if __name__ == '__main__':
#     a = Solution()
#     b = a.validWordAbbreviation("internationalization", "i12iz4n")
#     print(b)
# @lc code=end

