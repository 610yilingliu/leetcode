#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    # Is there any digit inside the bucket? i.e. [3a] or [2]
    # so we need to return a decoded string rather than its length, right?
    # (write the green command, type and rtype)
    # Is that possible for user to input an empty string, a single number or other invalid things like a]222?
    # nested brackets?
    # if yes we need a valid function

    # version 1
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        curnum = 0
        curstring = ''
        stack = []
        for char in s:
            if char == '[':
                stack.append(curstring)
                stack.append(curnum)
                curstring = ''
                curnum = 0
            elif char == ']':
                prenum = stack.pop()
                prestring = stack.pop()
                curstring = prestring + prenum * curstring
            elif char.isdigit():
                curnum = curnum * 10 + int(char)
            else:
                curstring += char
        return curstring


# @lc code=end

