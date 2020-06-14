#
# @lc app=leetcode id=917 lang=python3
#
# [917] Reverse Only Letters
#

# @lc code=start
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        N = len(S)
        l = N - 1
        res = ""
        for i, s in enumerate(S):
            if s.isalpha():
                while not S[l].isalpha():
                    l -= 1
                res += S[l]
                l -= 1
            else:
                res += s
        return res


class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        N = len(S)
        left, right = 0, N - 1
        slist = list(S)
        while left < right:
            while left < N and (not S[left].isalpha()):
                left += 1
            while right >= 0 and (not S[right].isalpha()):
                right -= 1
            if left < N and right >= 0 and left < right:
                slist[left], slist[right] = slist[right], slist[left]
            left, right = left + 1, right - 1
        return "".join(slist)

# @lc code=end

