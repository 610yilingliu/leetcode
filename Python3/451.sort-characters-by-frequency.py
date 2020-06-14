#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

import collections
# @lc code=start
class Solution:
    def frequencySort(self, s: str):
        if not s:
            return ''
        d = collections.Counter(s)
        ls = [[val, key] for key, val in d.items()]
        ls.sort(key = lambda x:(-x[0], x[1]))
        ans = ''
        for item in ls:
            ans += item[1] * item[0]
        return ans

if __name__ == '__main__':
    a = Solution()
    b = a.frequencySort("tree")
    print(b)


# @lc code=end

