class Solution:
    def exponential(self, x):
        if x == 0:
            return 1
        # it is obvious that the first item 1 is grater than 0.01, so we can start from 1 directly
        curbase = 1
        curk = 1
        while True:
            up = x ** curk
            down = self.factorial(curk)
            # if up/down < 0.01, break
            if up * 100 < down:
                curbase += up/down
                return round(curbase, 3)
            curbase += up/down
            curk += 1

    def factorial(self, n):
        if n == 0:
            return 0
        cur = 1
        for i in range(1, n + 1):
            cur *= i
        return cur


if __name__ == '__main__':
    a = Solution()
    b = a.exponential(1)
    print(b)