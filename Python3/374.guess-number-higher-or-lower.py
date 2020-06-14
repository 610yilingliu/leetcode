#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int):
        def binarysearch(start, end):
            mid = (start + end)//2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                return binarysearch(mid + 1, end)
            else:
                return binarysearch(start, mid)
        return binarysearch(1, n + 1)


# @lc code=end

