#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#

# @lc code=start
class Solution:
    def wordBreak(self, s, wordDict):
        # # O(2 ^ n)
        # dp = [False] * (len(s) + 1)
        # dp[0] = True
        # words = wordDict
        # result = []
        # def backtracker(dp, path, start = 0):
        #     if dp[-1]:
        #         result.append(' '.join(path))
        #     for i in range(start + 1, len(dp)):
        #             cur = s[start:i]
        #             if cur in words:
        #                 next_dp = dp.copy()
        #                 next_dp[i] = True
        #                 backtracker(next_dp, path + [cur], i)
        # backtracker(dp, [])
        # return result
        if not s:
            return []
        def searcher(s, words, visited):
            if s in visited:
                return visited[s]
            if not s:
                return []
            ans = []
            for word in words:
                if not s.startswith(word):
                    continue
                if len(word) == len(s):
                    ans.append(word)
                else:
                    res = searcher(s[len(word):], words, visited)
                    for item in res:
                        item = word + ' ' + item
                        ans.append(item)
            visited[s] = ans
            return ans
                    
        return searcher(s, wordDict, {})


if __name__ == '__main__':
    a = Solution()
    b = a.wordBreak("catsanddog",["cat", "cats", "and", "sand", "dog"])
    print(b)
# @lc code=end

