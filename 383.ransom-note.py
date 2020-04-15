#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote, magazine):
        if len(ransomNote) > len(magazine):
            return False
        letters = {}
        for c in magazine:
            letters[c] = letters[c] + 1 if c in letters else 1
        for c in ransomNote:
            if c not in letters:
                return False
            letters[c] -= 1
            if letters[c] < 0:
                return False
        return True


# @lc code=end

