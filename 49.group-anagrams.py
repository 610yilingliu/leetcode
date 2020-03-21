#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs):
        ans = []
        sorted_dict = dict()
        for i, word in enumerate(strs):
            s = sorted(list(word))
            item = "".join(s)
            if item not in sorted_dict:
                sorted_dict[item] = [i]
            else:
                sorted_dict[item] = sorted_dict[item] + [i]
        for k in sorted_dict:
            idxs = sorted_dict[k]
            inside = []
            for i in idxs:
                inside.append(strs[i])
            ans.append(inside)
        return ans


# @lc code=end
