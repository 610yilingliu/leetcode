#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1, nums2):
        if not nums1 or not nums2:
            return []
        d1 = dict()
        d2 = dict()
        while nums1:
            i1 = nums1.pop()
            if i1 not in d1:
                d1[i1] = 1
            else:
                d1[i1] += 1
        while nums2:
            i2 = nums2.pop()
            if i2 not in d2:
                d2[i2] = 1
            else:
                d2[i2] += 1
        ans = []
        for key in d1:
            if key in d2:
                num = min(d1[key], d2[key])
                for _ in range(num):
                    ans.append(key)
        return ans

if __name__ =='__main__':
    a = Solution()
    b = a.intersect([1,2,2,1], [2,2])
    print(b)


    # @lc code=end

