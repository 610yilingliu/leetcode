#
# @lc app=leetcode id=838 lang=python3
#
# [838] Push Dominoes
#

# @lc code=start
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        l = 0
        ans = []
        dominoes = 'L' + dominoes + 'R'
        for r in range(1, len(dominoes)):
            if dominoes[r] == '.':
                continue
            cnt = r - l - 1
            if l > 0:
                ans.append(dominoes[l])
            if dominoes[l] == dominoes[r]:
                ans.append(dominoes[l] * cnt)
            elif dominoes[l] == 'L' and dominoes[r] == 'R':
                ans.append('.' * cnt)
            else:
                ans.append('R' * (cnt // 2) + '.' * (cnt % 2) + 'L' * (cnt // 2))
            l = r
        return ''.join(ans)

if __name__ == '__main__':
    a = Solution()
    b = a.pushDominoes(".L.R...LR..L..")
    print(b)


# @lc code=end

