def arranging(ls):
    ls.sort()
    odd = []
    even = []
    for num in ls:
        if num & 1:
            odd.append(num)
        else:
            even.append(num)
    return odd, even

if __name__ == '__main__':
    lss = arranging([9,22,33,44,77,66,55,12,1])
    print(lss)

    