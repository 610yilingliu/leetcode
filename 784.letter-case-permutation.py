#
# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
#

# @lc code=start
class Solution:
    def letterCasePermutation(self, S):
        if not S:
            return []
        ans = [""]
        digit = {str(item) for item in range(10)}
        for c in S:
            temp = []
            if c in digit:
                for item in ans:
                    temp.append(item + c)
            else:
                for item in ans:
                    # temp.append(item + c.upper())
                    # temp.append(item + c.lower())
                    for char in [c.upper(), c.lower()]:
                        temp.append(item + char)
            ans = temp
        return ans

# class Solution(object):
#     def letterCasePermutation(self, S):
#         """
#         :type S: str
#         :rtype: List[str]
#         """
#         digits = {str(x) for x in range(10)}
#         A = ['']
#         for c in S:
#             B = []
#             if c in digits:
#                 for a in A:
#                     B.append(a+c)
#             else:
#                 for a in A:
#                     B.append(a+c.lower())
#                     B.append(a+c.upper())
#             A=B
#         return A

if __name__ == '__main__':
    a = Solution()
    b = a.letterCasePermutation("a1b2")
    print(b)



# @lc code=end

