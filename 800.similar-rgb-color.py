#
# @lc app=leetcode id=800 lang=python3
#
# [800] Similar RGB Color
#

# @lc code=start
class Solution:
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        def getClosest(s):
            m = ['00','11','22','33','44','55','66','77','88','99','aa','bb','cc','dd','ee','ff']
            return min(m, key = lambda x: abs(int(x, 16)- int(s,16)))
        
        res = ''
        color = color[1:]
        for i in range(3):
            s = color[2*i:2*i+2]
            res += getClosest(s)
        return '#' +res



# @lc code=end

