#
# @lc app=leetcode id=248 lang=python3
#
# [248] Strobogrammatic Number III
#

# @lc code=start
class Solution:
    d = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}

    def strobogrammaticInRange(self, low: str, high: str):
        if int(low) > int(high):
            return 0
        if int(low) < 0:
            low = '0'
        min_l = len(low)
        max_l = len(high)
        if min_l == max_l:
            ans_ls = self.helper(min_l, min_l)
            res = len(ans_ls)
            for item in ans_ls:
                if int(item) < int(low) or int(item) > int(high):
                    res -= 1
            return res
        ans = 0
        for n in range(min_l + 1, max_l):
            ans += len(self.helper(n, n))
        
        head = self.helper(min_l, min_l)
        head_l = len(head)
        tail = self.helper(max_l, max_l)
        tail_l = len(tail)
        for num in head:
            if int(num) < int(low):
                head_l -= 1
        for num in tail:
            if int(num) > int(high):
                tail_l -= 1
        return head_l + ans + tail_l

    def helper(self, n, current):
        if current == 0:
            return ['']
        if current == 1:
            return ['0', '1', '8']
        res = []
        for num in self.helper(n, current - 2):
            for k, v in self.d.items():
                if current != n or k != '0':
                    res.append(k + num + v)
        return res

# @lc code=end

if __name__ == '__main__':
    a = Solution()
    b = a.strobogrammaticInRange("50", "100")
    print(b)