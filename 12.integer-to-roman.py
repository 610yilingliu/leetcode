#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int):
        d =  {
            1: 'I',
            5 : 'V',
            10 : 'X',
            50 : 'L',
            100 : 'C',
            500: 'D',
            1000: 'M'
        }
        l = [1, 5, 10, 50, 100, 500, 1000]
        for idx in range(len(l) - 1, -1, -1):
            if num // l[idx] > 0:
                ans = self.helper(num, d, l, idx, '')
                break
        return ans


    def helper(self, num, d, l, pos, ans):
            num = num
            if num < 4:
                return ans + num * d[1]
            if num == 4:
                return ans + 'IV'
            if pos <= 0:
                return ans
            elif num//l[pos] < 4 and num%l[pos] == 0:
                return ans + d[l[pos]] * (num//l[pos])
            elif num >= 1000 and num%1000 == 0:
                return 'M' * num//1000
            elif num > 1000:
                time = num // 1000
                ans = d[1000] * time
                num = num - time * 1000
                pos = pos - 1
                return self.helper(num, d, l, pos, ans)
            else:
                if pos%2 == 1:
                    if num >= l[pos + 1] - l[pos - 1]:
                        ans = ans + d[l[pos - 1]] + d[l[pos + 1]]
                        num = num - (l[pos + 1] - l[pos - 1])
                        pos = pos - 1
                        return self.helper(num, d, l, pos, ans)
                    else:
                        time = num // l[pos]
                        ans = ans + d[l[pos]] * time
                        num = num % l[pos]
                        pos = pos - 1
                        return self.helper(num, d, l, pos, ans)
                else:
                    # pos = 0 is already returned in the previous condition
                    if num >= l[pos + 1] - l[pos]:
                        ans = ans + d[l[pos]] + d[l[pos + 1]]
                        num = num - (l[pos + 1] - l[pos])
                        pos = pos - 1
                        return self.helper(num, d, l, pos, ans)
                    else:
                        time = num // l[pos]
                        ans = ans + d[l[pos]] * time
                        num = num % l[pos]
                        pos = pos - 1
                        return self.helper(num, d, l, pos, ans)

if __name__ == '__main__':
    a = Solution()
    b = a.intToRoman(40)
    print(b)


# @lc code=end

