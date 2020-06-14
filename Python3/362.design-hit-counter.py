#
# @lc app=leetcode id=362 lang=python3
#
# [362] Design Hit Counter
#
import collections
# @lc code=start
class HitCounter:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = collections.deque()     
        

    def hit(self, timestamp: 'int') -> 'None':
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.data.append(timestamp)
        

    def getHits(self, timestamp: 'int') -> 'int':
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """        
        while self.data and timestamp - self.data[0] >= 300:
            self.data.popleft()
        return len(self.data)



# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# ls = [[1],[2],[3],[300],[301]]
# for param in ls:
#     obj.hit(param[0])
#     print(obj.q)
# # param_2 = obj.getHits(timestamp)
# @lc code=end

