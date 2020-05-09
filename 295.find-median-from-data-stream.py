#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize data structure
        """
        # Heap contains larger numbers
        self.bigger = []
        # Heap contains smaller numbers
        self.smaller = []
        # Time to push element into heaps, once uses addNum(), self.time += 1
        self.time = 0

    def addNum(self, num):
        '''
        Add a number into medianfinder() object
        '''
        # if no element in both 2 heaps, put it into bigger
        if not self.bigger and not self.smaller:
            self.bigger.append(num)
        # we need to keep len(bigger) == len(smaller) or len(bigger) - len(smaller) == 1
        elif len(self.bigger) - len(self.smaller) == 1:
            # len(bigger) - len(smaller) == 0 after this elif
            temp = heapq.heappop(self.bigger)
            if temp >= num:
                heapq.heappush(self.bigger, temp)
                # why use -num instead of num: in python, heap put smallest number in front of the list so we can use heap[0] to get it
                heapq.heappush(self.smaller, -num)
            else:
                heapq.heappush(self.bigger, num)
                heapq.heappush(self.smaller, -temp)
        else:
            # keep len(bigger) - len(smaller) == 1 after this else
            if num < self.bigger[0]:
                temp = heapq.heappop(self.smaller)
                temp = -temp
                if temp >= num:
                    heapq.heappush(self.bigger, temp)
                    heapq.heappush(self.smaller, -num)
                else:
                    heapq.heappush(self.bigger, num)
                    heapq.heappush(self.smaller, -temp)
            else:
                heapq.heappush(self.bigger, num)
        # count + 1 after adding elements
        self.time += 1

    def findMedian(self):
        '''
        Find the current median number
        '''
        if self.time & 1:
            return self.bigger[0]
        # remember elements in smaller is the opposite of the element we need to use, so use bigger[0] - smaller[0] instead of bigger[0] + smaller[0]
        return (self.bigger[0] - self.smaller[0])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(-1)
# obj.addNum(-2)
# obj.addNum(-3)
# obj.addNum(-4)
# obj.addNum(-5)
# param_2 = obj.findMedian()
# print(param_2)
# @lc code=end

