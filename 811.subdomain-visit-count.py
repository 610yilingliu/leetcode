#
# @lc app=leetcode id=811 lang=python3
#
# [811] Subdomain Visit Count
#

# @lc code=start
import collections

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        if not cpdomains:
            return []
        d = collections.defaultdict(int)
        for item in cpdomains:
            time, domain = item.split(' ')
            time = int(time)
            subdo = domain.split('.')
            pointer = len(subdo) - 1
            while pointer >= 0:
                curstr = '.'.join(subdo[pointer:])
                d[curstr] += time
                pointer -= 1
        ans = []
        for key, val in d.items():
            ans.append(str(val) + ' ' + key)
        return ans

# @lc code=end

