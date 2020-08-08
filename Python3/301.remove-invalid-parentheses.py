#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#

# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s):
            cursum = 0
            for x in s:
                if x == '(':
                    cursum += 1
                if x == ')':
                    cursum -= 1
                if cursum < 0:
                    return False
            return cursum == 0
        
        # BFS:
        cur_level = set()
        cur_level.add(s)
        while True:
            valids = list(filter(isValid, cur_level))
            if valids:
                return valids
            next_level = set()
            for s in cur_level:
                # 遍历所有删掉一个括号的情况
                for i in range(len(s)):
                    if s[i] in ['(', ')']:
                        next_level.add(s[:i] + s[i + 1 :])
            cur_level = next_level

        

        

# @lc code=end

