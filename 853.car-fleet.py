#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
class Solution:
    def carFleet(self, target, position, speed):
        cars = [(pos, s) for pos, s in zip(position, speed)]
        cars = sorted(cars, reverse = True)
        time = [(target - pos)/s for pos, s in cars]
        arrive = []
        for item in time:
            if not arrive:
                arrive.append(item)
            else:
                if item > arrive[-1]:
                    arrive.append(item)
        return len(arrive)

if __name__ == '__main__':
    a = Solution()
    b = a.carFleet(10, [0,4,2], [2,1,3])
    print(b)
# @lc code=end

