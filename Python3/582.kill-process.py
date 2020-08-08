#
# @lc app=leetcode id=582 lang=python3
#
# [582] Kill Process
#
import collections
# @lc code=start
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int):
        children = collections.defaultdict(list)
        for i in range(len(pid)):
            children[ppid[i]].append(pid[i])
        todo_ls = []
        todo_ls.append(kill)
        ans = []
        while todo_ls:
            temp_saver = []
            while todo_ls:
                curval = todo_ls.pop()
                if curval in children:
                    temp_saver += children[curval]
                ans.append(curval)
            todo_ls = temp_saver
        return ans


# @lc code=end

