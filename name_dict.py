def edic(keys, names, ages):
    d = dict()
    for i in range(len(keys)):
        d[keys[i]] = [names[i], ages[i]]
    return d

if __name__ == '__main__':
    res = edic([11, 22],['Alice', 'Ben'],[45, 49])
    print(res)