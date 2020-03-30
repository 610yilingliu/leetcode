#
# @lc app=leetcode id=401 lang=python3
#
# [401] Binary Watch
#

# @lc code=start
class Solution:
    def readBinaryWatch(self, num):
        self.ans_ls = []
        self.helper(num, 0, [])
        ans = []
        for item in self.ans_ls:
            m = 0
            h = 0
            for num in item:
                if num >= 4:
                    num -= 4
                    m += (1 << num)
                else:
                    h += (1 << num)
            if m == 0:
                m_str = '00'
            elif m < 10:
                m_str = '0' + str(m)
            elif m > 59:
                continue
            else:
                m_str = str(m)
            if h > 11:
                continue
            else:
                h_str = str(h)
            ans.append(h_str + ':' + m_str)
        return ans 

    def helper(self, n, cur, ls):
        if 10 - cur < n:
            return
        if n == 0:
            self.ans_ls.append(ls)
        for elem in range(cur, 10):
            self.helper(n - 1, elem + 1, [elem] + ls)

if __name__ == '__main__':
    a = Solution()
    b = a.readBinaryWatch(2)
    print(b)
# @lc code=end

