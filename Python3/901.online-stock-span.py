#
# @lc app=leetcode id=901 lang=python3
#
# [901] Online Stock Span
#

# @lc code=start
class StockSpanner:

    def __init__(self):
        self.a = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        res = 1
        while self.a and self.a[-1][0] <= price:
            res += self.a.pop()[1]
        self.a.append((price, res))
        return res

# https://blog.csdn.net/fuxuemingzhu/article/details/82781059
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# ls = [[31],[41],[48],[59],[79]]
# for item in ls:
#     param_1 = obj.next(item[0])
#     print(param_1)
# print(obj.prices)
# @lc code=end

