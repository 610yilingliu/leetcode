#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
import heapq
class Solution:
    def nextGreatestLetter(self, letters, target):
        curheap = []
        heapq.heappush(letters, target)
        for letter in letters:
            heapq.heappush(curheap, letter)
        head = heapq.heappop(curheap)
        if head == target:
            nxt = heapq.heappop(curheap)
            while nxt == head and curheap:
                nxt = heapq.heappop(curheap)
            return nxt
        tar = heapq.heappop(curheap)
        while tar != target:
            tar = heapq.heappop(curheap)
        if not curheap:
            return head
        ans = heapq.heappop(curheap)
        while ans == target and curheap:
            ans = heapq.heappop(curheap)
        if ans == target:
            return head
        return ans
        

# if __name__ == '__main__':
#     a = Solution()
#     b = a.nextGreatestLetter(["c","f","j"], "g")
#     print(b)
# @lc code=end

