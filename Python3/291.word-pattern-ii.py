#
# @lc app=leetcode id=291 lang=python3
#
# [291] Word Pattern II
#

# @lc code=start
class Solution:
    def wordPatternMatch(self, pattern, str):
        return self.finder({},{},pattern,str,0,0)

    
    def finder(self, p2s, s2p, p, s, pp, sp):
        matched = False
        if pp == len(p) and sp == len(s):
            matched = True
        elif pp < len(p) and sp < len(s):
            cur_p = p[pp]
            if cur_p in p2s:
                curword = p2s[cur_p]
                if curword == s[sp:sp + len(curword)]:
                    matched = self.finder(p2s, s2p, p, s, pp + 1, sp + len(curword))
            else:
                for i in range(sp, len(s)):
                    curword = s[sp:i + 1]
                    if curword not in s2p:
                        s2p[curword] = cur_p
                        p2s[cur_p] = curword
                        matched = self.finder(p2s, s2p, p, s, pp + 1, i + 1)
                        s2p.pop(curword)
                        p2s.pop(cur_p)
                    if matched:
                        break
        return matched

# if __name__ == '__main__':
#     a = Solution()
#     b = a.wordPatternMatch("dogcatcatdog", 'abba')
#     print(b)

# @lc code=end

