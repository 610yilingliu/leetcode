#
# @lc app=leetcode id=359 lang=python3
#
# [359] Logger Rate Limiter
#

# @lc code=start
class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = dict()

    def shouldPrintMessage(self, timestamp: int, message: str):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.d:
            self.d[message] = timestamp
            return True
        if timestamp - self.d[message] < 10:
            return False
        self.d[message] = timestamp
        return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
# @lc code=end

