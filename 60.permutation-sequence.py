#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#

# @lc code=start
class Solution:
    def getPermutation(self, n, k):
        if n == 0:
            return '0'
        if n == 1:
            return str(n)
        nums = []
        for i in range(n):
            nums.append(str(i + 1))
        if k == 1:
            return "".join(nums)
        div = 1
        for i in range(1, n+1):
            div = div * i
        print(div)
        if k % div !=0:
            k = k % div
        else:
            k = div
        ans = self.generator(nums, 1, k)
        ans = "".join(ans)
        return ans
    
    def generator(self, nums, time, dist):
        if time == dist:
            return nums
        l = -1
        r = -1
        for i in range(len(nums)-1 , 0, -1):
            if nums[i - 1] < nums[i]:
                l = i - 1
                break
        if l == -1:
            time = time + 1
            nums = nums[::-1]
            self.generator(nums, time, dist)
        for i in range(len(nums) - 1, l, -1):
            if nums[i] > nums[l]:
                r = i
                break
        nums[l], nums[r] = nums[r], nums[l]
        prefix = nums[:l + 1]
        suffix = nums[l+1:]
        if suffix:
            suffix.sort()
        nums = prefix + suffix
        time = time + 1
        return self.generator(nums, time, dist)

if __name__ == '__main__':
    a = Solution()
    b = a.getPermutation(9,171669)
    print(b)



# @lc code=end

