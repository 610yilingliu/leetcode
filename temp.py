
def guess():
    for curans in range(1, 101):
        man = 0
        for num in range(1, 101):
            if num == curans:
                man += 1
        if man == 100 - curans:
            return curans

if __name__ == '__main__':
    a = guess()
    # result: 99
    print(a)
