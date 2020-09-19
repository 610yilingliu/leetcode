#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

import collections
# @lc code=start
class Solution:
      def partitionLabels(self, S):
        ans = []
        start, end = 0, 0
        for i in range(len(S)):
            end = max(end, S.rfind(S[i]))
            if i == end:
                ans.append(end - start + 1)
                start = end + 1
        return ans

a = Solution()
b = a.partitionLabels("ababcbacadefegdehijhklij")
            

# @lc code=end

