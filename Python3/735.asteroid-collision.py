#
# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#
import collections
# @lc code=start
class Solution:
    def asteroidCollision(self, asteroids: List[int]):
        r_stack = collections.deque();
        idx = len(asteroids) - 1
        while asteroids and idx >= 0:
            r_stack.appendleft(asteroids.pop())
            while r_stack and asteroids:
                if r_stack[0] < 0 and asteroids[-1] > 0:
                    if abs(r_stack[0]) < abs(asteroids[-1]):
                        r_stack.popleft()
                    elif abs(r_stack[0]) > abs(asteroids[-1]):
                        asteroids.pop()
                    else:
                        r_stack.popleft()
                        asteroids.pop()
                else:
                    break
            idx -= 1
        return r_stack
# @lc code=end

