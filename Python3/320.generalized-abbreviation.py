#
# @lc app=leetcode id=320 lang=python3
#
# [320] Generalized Abbreviation
#

# @lc code=start
class Solution:
    def generateAbbreviations(self, word: str):
        if not word:
            return [""]
        ans = ['']
        for i in range(len(word)):
            temp = []
            for item in ans:
                temp.append(item + word[i])
                if not item:
                    temp.append('1')
                elif item[-1].isdigit():
                    temp.append(item[:-1] + str(int(item[-1]) + 1))
                else:
                    temp.append(item + '1')
            ans = temp
        return ans

if __name__ == '__main__':
    a = Solution()
    b = a.generateAbbreviations('word')
    print(b)



# @lc code=end

