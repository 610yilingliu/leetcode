#
# @lc app=leetcode id=1291 lang=python3
#
# [1291] Sequential Digits
#

# @lc code=start
class Solution:
    def sequentialDigits(self, low, high):
        if low == high == 0 or high < low:
            return []
        start_len = len(str(low))
        end_len = len(str(high))
        start_first = int(str(low)[0]) if int(str(low)[0]) != 0 else 1
        end_first = int(str(high)[0])
        ans = []
        ans = ans + self.generate(start_len, start_first, start = low, end = high)
        for i in range(start_len + 1, end_len):
            ans = ans + self.generate(i, 1)
        if start_len != end_len:
            ans = ans + self.generate(end_len, 1, end = high)
        return ans


    def generate(self, digits, start_dig, start = None, end = None):
        res = []
        for i in range(start_dig, 10 - digits + 1 ):
            added = 1
            cur = i
            cnt = i
            while added < digits:
                cur = cur * 10 + cnt + 1
                added += 1
                cnt += 1
            if start is not None and start > cur:
                continue
            elif end is not None and end < cur:
                break
            else:
                res.append(cur)
        return res

# if __name__ == '__main__':
#     a = Solution()
#     b = a.sequentialDigits(58, 155)
#     print(b)
# @lc code=end

