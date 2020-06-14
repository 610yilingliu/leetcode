#
# @lc app=leetcode id=397 lang=python3
#
# [397] Integer Replacement
#

# @lc code=start
class Solution:
    def integerReplacement(self, n):
        if n < 2:
            return 0
        step = 0
        while n >= 2:
            if n == 3:
                return step + 2
            if n & 1 == 1: 
                if self.onecounter(n + 1) < self.onecounter(n - 1):
                    n += 1
                elif self.onecounter(n + 1) > self.onecounter(n - 1):
                    n -= 1
                else:
                    time = 2
                    while time < 32:
                        plus = self.onecounter((n + 1), time)
                        minus = self.onecounter((n - 1), time)
                        if plus > minus:
                            n -= 1
                            break
                        elif plus < minus:
                            n += 1
                            break
                        else:
                            time += 1
                step += 1
            else:
                n >>= 1
                step += 1
        return step

    def onecounter(self, num, n = 1):
        max_bit = n
        count = 0
        while max_bit > 0:
            num >>= 1
            if num & 1 == 1:
                count += 1
            max_bit -= 1
        return count

if __name__ == '__main__':
    a = Solution()
    b = a.integerReplacement(100000000)
    print(b)
# @lc code=end

