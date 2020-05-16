#
# @lc app=leetcode id=255 lang=python3
#
# [255] Verify Preorder Sequence in Binary Search Tree
#

# @lc code=start
class Solution:
    def verifyPreorder(self, preorder):
        q = []
        curmin = None
        for node in preorder:
            while q and node > q[-1]:
                curmin = q.pop()
            if curmin!= None and node < curmin:
                return False
            q.append(node)
        return True



if __name__ == '__main__':
    a = Solution()
    b = a.verifyPreorder([5,2,6,1,3])
    print(b)


# @lc code=end

