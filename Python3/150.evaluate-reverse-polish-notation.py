#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens):
        stack = []
        ops = ['+', '-', '*', '/']
        for num in tokens:
            if num not in ops:
                stack.append(num)
            else:
                b = stack.pop()
                a = stack.pop()
                if num == '/' and int(a) * int(b) < 0:
                    cur = eval(a + num + b)
                    intdiv = eval(a + '//' + b)
                    if float(intdiv) != cur:
                        intdiv += 1
                    stack.append(str(intdiv))
                else:
                    cur = int(eval(a + num + b))
                    stack.append(str(cur))
        return int(stack.pop())

if __name__ == '__main__':
    a = Solution()
    b = a.evalRPN(["4", "13", "5", "/", "+"])
    print(b)
# @lc code=end

