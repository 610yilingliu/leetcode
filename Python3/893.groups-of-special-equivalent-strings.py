#
# @lc app=leetcode id=893 lang=python3
#
# [893] Groups of Special-Equivalent Strings
#

# @lc code=start
class Solution:
    def numSpecialEquivGroups(self, A):
        d = set()
        for item in A:
            cur_raw = ''.join(sorted(item[0::2])) + ''.join(sorted(item[1::2]))
            d.add(cur_raw)
        return len(d)

if __name__ == '__main__':
    a = Solution()
    b = a.numSpecialEquivGroups(["abcd","cdab","cbad","xyzz","zzxy","zzyx"])
    print(b)

# @lc code=end

