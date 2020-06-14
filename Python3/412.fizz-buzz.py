#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        if n <= 0:
            return ans
        for num in range(1, n + 1):
            if num % 3 == 0 and num % 5 == 0:
                ans.append('FizzBuzz')
            elif num % 3 == 0:
                ans.append('Fizz')
            elif num % 5 == 0:
                ans.append('Buzz')
            else:
                ans.append(str(num))
        return ans
# @lc code=end

