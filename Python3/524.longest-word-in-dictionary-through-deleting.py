#
# @lc app=leetcode id=524 lang=python3
#
# [524] Longest Word in Dictionary through Deleting
#

# @lc code=start
class Solution:
    def findLongestWord(self, s, d):
        if not s or not d:
            return ""
        d.sort(key = lambda x: (-len(x), x))
        ans = ""
        for item in d:
            p1 = 0
            p2 = 0
            while p1 < len(s) and p2 < len(item):
                if s[p1] == item[p2]:
                    p2 += 1
                p1 += 1
            if p2 == len(item):
                if ans == "":
                    ans = item
                    break
        return ans

if __name__ == '__main__':
    a = Solution()
    b = a.findLongestWord("abpcplea", ["ale","apple","aaaaa","monkey","plea"])
    print(b)

# @lc code=end

