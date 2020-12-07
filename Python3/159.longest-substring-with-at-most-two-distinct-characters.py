#
# @lc app=leetcode id=159 lang=python3
#
# [159] Longest Substring with At Most Two Distinct Characters
#
# @lc code=start
# class Solution:
#     def lengthOfLongestSubstringTwoDistinct(self, s: str):
#         curset = set()
#         curstring = []
#         ans = 0
#         for i in range(len(s)):
#             if s[i] not in curset and len(curset) < 2:
#                 curset.add(s[i])
#                 curstring.append(s[i])
#             elif s[i] in curset:
#                 curstring.append(s[i])
#             else:
#                 ans = max(ans, len(curstring))
#                 keep = curstring[-1]
#                 for j in range(len(curstring)-1, -1, -1):
#                     if curstring[j]!= keep:
#                         break
#                 curstring = curstring[j + 1:]
#                 todel = ''
#                 for k in curset:
#                     if k != keep:
#                         todel = k
#                         break
#                 curset.remove(todel)
#                 curstring.append(s[i])
#                 curset.add(s[i])
                
#         ans = max(ans, len(curstring))
#         return ans

# if __name__ == '__main__':
#     a = Solution()
#     b = a.lengthOfLongestSubstringTwoDistinct("ababffzzeee")
#     print(b)

# what should we return if it is an empty string?
# maximum: 2
# should return the **length** of the longest substring, not that substring itself
# will use python, no overflow

import collections

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: String
        :rtype: int
        """
        mxlen = 0
        lp, rp = 0, 0
        tool_dict = collections.defaultdict(int)
        tool_set = set()
        while rp < len(s):
            tool_dict[s[rp]] += 1
            tool_set.add(s[rp])
            if len(tool_set) > 2:
                mxlen = max(mxlen, rp - lp)
                while lp < rp and len(tool_set) > 2:
                    tool_dict[s[lp]] -= 1
                    if tool_dict[s[lp]] == 0:
                        tool_set.remove(s[lp])
                    lp += 1
            rp += 1
        mxlen = max(mxlen, rp - lp)
        return mxlen

        
# @lc code=end

