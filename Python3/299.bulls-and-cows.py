#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
#

# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str):
        d = dict()
        l = len(secret)
        for i in range(l):
            if secret[i] not in d:
                d[secret[i]] = 1
            else:
                d[secret[i]] += 1
        A = 0
        B = 0
        for i in range(l):
            if guess[i] == secret[i]:
                A += 1
                d[guess[i]] -= 1
        for i in range(l):
            if guess[i] != secret[i] and guess[i] in d and d[guess[i]] > 0:
                B += 1
                d[guess[i]] -= 1
        return str(A) + 'A' + str(B) + 'B'


        
# @lc code=end

