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
            # prevent from spaces at the start/end of each cell, example: '123   '
            line = line.strip()
            line = line.split(',')
            for cell in line:
                # skip empty cell
                if not cell:
                    continue
                # prevent error from i = 10, cell = '12'
                if i < len(cell):
                    # if cell[i] is a number
                    if cell[i].isnumeric():
                        # trick
                        data_counter[int(cell[i])] = data_counter.get(int(cell[i]), 0) + 1
                    # if cell[i] is not numeric, for example, for 56.123, cell[2] == '.', we should not do anything with the following '123', so set the whole string as
                    # an empyt one, for the next loop, we can use line 19 to skip it
                    else:
                        cell = ''
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



