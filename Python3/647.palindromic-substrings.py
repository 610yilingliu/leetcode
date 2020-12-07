#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    # Q: what is your def of a palindromic string? Would you give me a few more example?
    # Q: You just want the number of valid substring or you want me to return or yield all the valid strings?
    # Q: edge case: what should we return if the given string is empty, or no palindromic substring in the given string? None or 0?

    # version 1: the way that is slow but straight and it works.
    # def countSubstrings(self, s):
    #     """
    #     main function
    #     :type s: String
    #     :rtype: Int, number of valid substrings.
    #     """
    #     ans = 0
    #     for i in range(len(s)):
    #         p1 = i
    #         p2 = i
    #         while p2 >= 0 and p1 < len(s):
    #             if s[p1] == s[p2]:
    #                 ans += 1
    #                 p1 += 1
    #                 p2 -= 1
    #             else:
    #                 break

    #         p3 = i
    #         p4 = i - 1
    #         while p4 >= 0 and p3 < len(s):
    #             if s[p3] == s[p4]:
    #                 ans += 1
    #                 p3 += 1
    #                 p4 -= 1
    #             else:
    #                 break
    #     # time comp: O(n^2)
    #     return ans
    
    # version 2
    def countSubstrings(self, s):
        """
        main function
        :type s: String
        :rtype: Int, number of valid substrings.
        """
        s = "~#" + '#'.join(s) + '#!'
        # dp: record the longest palindromic string radius in the current position
        dp = [0] * len(s)
        center = right = 0
        for i in range(1, len(s) - 1):
            if i < right:
                dp[i] = min(right - i, dp[2 * center - i])
            while s[i + dp[i] + 1] == s[i - dp[i] - 1]:
                dp[i] += 1
            if i + dp[i] > right:
                center = i
                right = dp[i] + i
        return sum((l + 1)//2 for l in dp)


    
# a = Solution()
# b = a.countSubstrings("aaa")
# print(b)
# @lc code=end

