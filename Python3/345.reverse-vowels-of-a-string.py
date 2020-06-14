#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s):
        if len(s) <2:
            return s
        # vowels: a, e, i, o, u
        v = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        pref = ''
        suff = ''
        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and s[j] not in v:
                suff = s[j] + suff
                j -= 1
            while i < j and s[i] not in v:
                pref = pref + s[i]
                i += 1
            pref = pref + s[j]
            suff = s[i] + suff
            if i == j:
                return pref[: -1] + suff
            i += 1
            j -= 1
        if i == j:
            return pref + s[i] + suff
        return pref + suff
        
        

if __name__ == '__main__':
    a = Solution()
    b = a.reverseVowels(".a")
    print(b)
    

# @lc code=end

