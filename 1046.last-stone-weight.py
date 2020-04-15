#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start
class Solution:
    def lastStoneWeight(self, stones):
        if not stones:
            return 0
        stones.sort()
        while len(stones) > 1:
            biggest = stones.pop()
            biggest_2nd = stones.pop()
            if biggest > biggest_2nd:
                stones.append(biggest - biggest_2nd)
                stones.sort()
        if not stones:
            return 0
        return stones[0]

if __name__ == '__main__':
    a = Solution()
    b = a.lastStoneWeight([2,7,4,1,8,1])
    print(b)

# @lc code=end

