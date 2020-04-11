#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
# class Solution:
#     def isHappy(self, n: int):
#         appeared = {}
#         while True:
#             s = 0
#             while n > 0:
#                 s += (n % 10) * (n % 10)
#                 n = n//10
#             if s == 1:
#                 return True
#             else:
#                 if s not in appeared:
#                     appeared[s] = True
#                     n = s
#                 else:
#                     return False

class Solution:
    def isHappy(self, n):
        visited = set()
        re = self.helper(n, visited)
        return re
    def helper(self, n, visited):
        s = 0
        while n > 0:
            s = s + (n%10) ** 2
            n = n//10
        if s == 1:
            return True
        elif s in visited:
            return False
        else:
            visited.add(s)
            return self.helper(s, visited)

if __name__ == '__main__':
    a = Solution()
    b = a.isHappy(68)
    print(b)

# @lc code=end

