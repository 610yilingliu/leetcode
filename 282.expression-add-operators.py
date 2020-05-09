#
# @lc app=leetcode id=282 lang=python3
#
# [282] Expression Add Operators
#

# @lc code=start
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        def calculate(num, target, expression, prev, ans, results):
            if len(num) == 0 and ans == target:
                results.append(expression)
            else:
                for i in range(1, len(num)+1):
                    if i > 1 and num[0] == '0':
                        continue
                    a = int(num[0:i])
                    if expression == '':
                        calculate(num[i:len(num)], target, num[0:i], a, a, results)
                    else:
                        calculate(num[i:len(num)], target, expression+'+'+num[0:i], a, ans+a, results)
                        calculate(num[i:len(num)], target, expression+'-'+num[0:i], -a, ans-a, results)
                        calculate(num[i:len(num)], target, expression+'*'+num[0:i], a*prev, ans+prev*(a-1), results)
        
        
        results = []
        calculate(num, target, '', 0, 0, results)
        return results
# @lc code=end

