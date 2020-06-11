#
# @lc app=leetcode id=400 lang=python3
#
# [400] Nth Digit
#

# @lc code=start
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """

        N=1

        while n>0: 

            r= 9* 10**(N-1)*N

            if n>r:
                n-=r
                N+=1
            else:
                number= 10**(N-1) + (n-1)/N
                return int(str(number)[(n-1)%N])



# @lc code=end


# def merge(l1, l2):
#     ans = []
#     # 如果l1和l2都不为空
#     while l1 and l2:
#         # 如果l1的第一个元素小于等于l2的第二个元素
#         if l1[0] <= l2[0]:
#             # 将l1的第一个元素加入answer
#             ans.append(l1[0])
#             # 把l1中的第一个元素从l1中删除
#             l1.pop(0)
#         else:
#             ans.append(l2[0])
#             l2.pop(0)
#     # 如果剩下的，还有元素的列表是l1
#     if l1:
#         # 拼接ans和剩余l1
#         return ans + l1
#     # 如果剩余的列表是l2，拼接ans和l2
#     return ans + l2
        