#
# @lc app=leetcode id=267 lang=python3
#
# [267] Palindrome Permutation II
#

# @lc code=start
import collections
class Solution():
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        cnt = collections.Counter(s)
        if len(cnt) == 1:
            return [s]
        mid = ''
        for k in cnt:
            if cnt[k] & 1:
                mid += k
                cnt[k] -= 1
        if len(mid) > 1:
            return []

        chars = ''.join([k * (v >> 1) for k, v in cnt.items()])
        ans = set()
        def premutation(word, tmp):
            if not word:
                ans.add(tmp + mid + tmp[::-1])
                return
            for i in range(len(word)):
                premutation(word[:i] + word[i + 1:], tmp + word[i])
        premutation(chars, '')
        return ans



# if __name__ == '__main__':
#     a = Solution()
#     b = a.generatePalindromes("aaaabbbb")
#     print(b)

# @lc code=end

