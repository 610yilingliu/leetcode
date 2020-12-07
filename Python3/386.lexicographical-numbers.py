#
# @lc app=leetcode id=386 lang=python3
#
# [386] Lexicographical Numbers
#

# @lc code=start
class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def dfs(cur,n,res):  #cur是根节点
            if cur > n:
                return 
            else:
                res.append(cur)
                for i in range(10):
                    dfs(i+cur*10,n,res)
            
        res =[]
        for i in range(1,10):
            dfs(i,n,res)
        return res


# @lc code=end

