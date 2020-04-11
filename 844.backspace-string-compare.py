#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    def backspaceCompare(self, S: str, T: str):

        dps = [0] * len(S)
        dpt = [0] * len(T)
        if S[0] != '#':
            dps[0]= S[0]
        else:
            dps[0] = ''
        if T[0] != '#':
            dpt[0] = T[0]
        else:
            dpt[0] = ''
        for i in range(1, len(S)):
            if S[i] == '#':
                if len(dps[i - 1]) > 0:
                    dps[i] = dps[i - 1][:-1]
                else:
                    dps[i] = ''
            else:
                dps[i] = dps[i - 1] + S[i]
        for i in range(1, len(T)):
            if T[i] == '#':
                if len(dpt[i - 1]) > 0:
                    dpt[i] = dpt[i - 1][:-1]
                else:
                    dpt[i] = ''
            else:
                dpt[i] = dpt[i - 1] + T[i]
        return dps[-1] == dpt[-1]

if __name__ == '__main__':
    a = Solution()
    b = a.backspaceCompare("a##c", "#a#c")
    print(b)
# @lc code=end

