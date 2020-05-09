def is_valid(num):
    # num >> 1 相当于 num // 2，但是位运算更快。这里只是随便规定个范围，等会会用break跳出。因为要尽量避免开方（计算机中如果出现除法，开方之类速度特别慢）。我后面是用 i * i > num 来代替一开始就将i规定为（3,math.sqrt(num))
    # 需要从3开始，因为题目已经说明了没有1和2。同样，4,6,8...这些数字也不需要考虑，所以设置了step = 2（python中的range完整输入是range(start, end, step))
    for i in range(3, num >> 1, 2):
        # 跳出。不需要再判断是否能整除根号num以上的数，这是重复了前面的操作（3*5和5*3就是重复操作)
        if i * i > num:
            return False
        # 若能整除，则返回true跳出
        if num % i == 0:
            return True

def solution(n):
    # 1 的时候直接给答案，不用折腾了
    if n == 1:
        return 9
    curnum = 9
    count = 1
    while True:
        if is_valid(curnum):
            if count == n:
                return curnum
            count += 1
        # 还是2一跳， 因为只需要检查9,11,13...偶数肯定是不符合要求的
        curnum += 2

if __name__ == '__main__':
    a = solution(3)
    print(a)
