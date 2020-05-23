def singledigit(n):
    while n > 9:
        cursum = 0
        num = n
        while num > 0:
            cursum += num % 10
            num = num // 10
        n = cursum
    return n

if __name__ == '__main__':
    ans = singledigit(198)
    print(ans)