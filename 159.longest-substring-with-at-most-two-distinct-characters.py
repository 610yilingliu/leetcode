#
# @lc app=leetcode id=159 lang=python3
#
# [159] Longest Substring with At Most Two Distinct Characters
#
# @lc code=start
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str):
        curset = set()
        curstring = []
        ans = 0
        for i in range(len(s)):
            if s[i] not in curset and len(curset) < 2:
                curset.add(s[i])
                curstring.append(s[i])
            elif s[i] in curset:
                curstring.append(s[i])
            else:
                ans = max(ans, len(curstring))
                keep = curstring[-1]
                for j in range(len(curstring)-1, -1, -1):
                    if curstring[j]!= keep:
                        break
                curstring = curstring[j + 1:]
                todel = ''
                for k in curset:
                    if k != keep:
                        todel = k
                        break
                curset.remove(todel)
                curstring.append(s[i])
                curset.add(s[i])
                
        ans = max(ans, len(curstring))
        return ans

if __name__ == '__main__':
    a = Solution()
    b = a.lengthOfLongestSubstringTwoDistinct("ababffzzeee")
    print(b)
# @lc code=end

