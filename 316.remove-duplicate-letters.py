#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s):
        # with first and last idx of each char
        if not s:
            return ""
        ls = list(s)
        stack = []
        stack.append(ls.pop(0))
        while len(ls) > 0:
            item = ls.pop(0)
            if item not in stack:
                while len(stack) > 0 and item < stack[-1]:
                    if stack[-1] in ls:
                        stack.pop()
                    else:
                        break
                stack.append(item)
        return ''.join(stack)

if __name__ == '__main__':
    a = Solution()
    b = a.removeDuplicateLetters('bbcaac')
    print(b)
# @lc code=end

