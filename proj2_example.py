def readfile(fname):
    try:
        f = open(fname, 'r')
    except:
        print(fname + ' not exists')
        exit(0)
    content = f.readlines()
    f.close()
    return content

def clean(content, digit):
    numbers = []
    for i in range(digit):
        data_counter = dict()
        for line in content:
            for cell in line:
                # prevent from spaces at the start/end of each cell, example: '123   '
                cell = cell.strip()
                # if cell[i] is a number
                if cell[i].isnumeric():
                    # trick
                    data_counter[int(cell[i])] = data_counter.get(int(cell[i]), 0) + 1
                # if cell[i] is not numeric, for example, for 56.1, cell[2] == '.', we shoule stop the loop
                else:
                    break
        numbers.append(data_counter)
    return numbers

def analyzer(numbers, digit, regularise):
    ans = []
    for d in range(digit):
        distribution = [0] * 10
        current_dict = numbers[d]
        for key, value in current_dict.items():
            if key == 0:
                distribution[-1] = value
            else:
                distribution[key - 1] = value
        if regularise == False:
            ans.append(distribution)
        else:
            denominator = sum(distribution)
            for i in range(len(distribution)):
                distribution[i] = distribution[i]/denominator
            ans.append(distribution)
    return ans

def main(filename,no_places,regularise=False):
    file_content = readfile(filename)
    number_dict = clean(file_content)
    ans = analyzer(number_dict, no_places, regularise)
    return ans


    