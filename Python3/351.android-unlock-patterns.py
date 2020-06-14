#
# @lc app=leetcode id=351 lang=python3
#
# [351] Android Unlock Patterns
#

# @lc code=start
class Solution:
    def numberOfPatterns(self, m: int, n: int):
        self.res = 0
        all_set = set(range(1, 10))
        
        # cur_set:当前走过的所有点
        # prev:现在所在的点
        def backtrack(cur_set, prev):
            if len(cur_set) >= m:
                self.res += 1
                if len(cur_set) == n:
                    return
            # 由于手势里不能有重复的  所以在键盘里把已经走过的点排除出去
            # 剩下的作为新的目标点
            for num in all_set - cur_set:
                abs_t = abs(num - prev)
                # 水平方向  跨过一个数
                if abs_t == 2 and min(num, prev) in {1, 4, 7} and (num + prev) // 2 not in cur_set: continue
                # 右下方向  跨过一个数
                if abs_t == 4 and min(num, prev) == 3 and 5 not in cur_set: continue
                # 竖直方向  跨过一个数
                if abs_t == 6 and (num + prev) // 2 not in cur_set: continue
                # 左下方向  跨过一个数
                if abs_t == 8 and 5 not in cur_set: continue
                backtrack(cur_set | {num}, num)
        # 以键盘上的任何一个点作为起始点
        for i in range(1, 10):
            backtrack({i}, i)

        return self.res
if __name__ == '__main__':
    a = Solution()
    b = a.numberOfPatterns(1, 2)
    print(b)
        
            
# @lc code=end

