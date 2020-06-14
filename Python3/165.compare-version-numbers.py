#
# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#
import collections
# @lc code=start
class Solution:
    def compareVersion(self, version1, version2):
        v1 = version1.split('.')
        v2 = version2.split('.')
        if len(v1) > len(v2):
            longer = 1
            l = len(v2)
        else:
            longer = 2
            l = len(v1)
        for i in range(l):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
        if longer == 1:
            for item in range(l, len(v1)):
                if int(v1[item]) != 0:
                    return 1
        else:
            for item in range(l, len(v2)):
                if int(v2[item]) != 0:
                    return -1
        return 0

if __name__ == '__main__':
    a = Solution()
    b = a.compareVersion("1.0", "1")
    print(b)

# @lc code=end

