#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#

# @lc code=start
class Solution:
    def candy(self, ratings):
        if len(ratings) == 1:
            return 1
        if len(ratings) == 2:
            if ratings[0] == ratings[1]:
                return 2
            return 3
        candy = [0] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and candy[i] < candy[i + 1] + 1:
                candy[i] = candy[i + 1] + 1
        return sum(candy) + len(ratings)
        

if __name__ == '__main__':
    a = Solution()
    b = a.candy([1,3,4,5,2])
    print(b)
        
        

            
            
# @lc code=end

