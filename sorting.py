def listsort(name, age):
    d = dict()
    for i in range(len(name)):
        d[name[i]] = age[i]
    age.sort(reverse = True)
    result_name = []
    result_age = []
    for i in range(len(age)):
        for key, val in d.items():
            if val == age[i]:
                result_name.append(key)
                result_age.append(val)
                d.pop(key)
                break
    return (result_name, result_age)

if __name__ == '__main__':
    res = listsort(['a','b','c'], [1, 80, 20])
    print(res)