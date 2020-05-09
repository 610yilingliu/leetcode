#
# @lc app=leetcode id=313 lang=python3
#
# [313] Super Ugly Number
#

# @lc code=start
class Solution:
    def nthSuperUglyNumber(self, n, primes):
            ugly = [1]
            pointers = [0]*len(primes)
            
            for i in range(1,n):
                minu = float("inf")
                minIndex = 0
                for j in range(len(primes)):
                    if primes[j] * ugly[pointers[j]] < minu:
                        minu = primes[j] * ugly[pointers[j]]
                        minIndex = j
                    elif primes[j] * ugly[pointers[j]] == minu:
                        pointers[j] += 1
                ugly.append(minu)
                pointers[minIndex] += 1
            return ugly[-1]



# @lc code=end

