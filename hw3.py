# problem 0
def parse_input(input):
    try:
        return float(input)
    except:
        return None
    
# problem 1
def before_the_whale(filename):
    words_before_whale = set()

    with open(filename, 'r') as file:
        text = file.read()

    words = text.split()

    for i in range(1, len(words)):
        if 'whale' in words[i].lower():
            words_before_whale.add(words[i-1].strip('.,!?'))

    return list(words_before_whale)

# problem 2
def compressor(lst):
    new_lst = []

    current_int = lst[0]
    counter = 1
    for i in lst[1:]:
        if current_int==i:
            counter+=1
        else:
            new_lst += [counter, current_int]
            current_int = i
            counter = 1

    new_lst += [counter, current_int]
    return new_lst
            
# problem 3
def compressor_reverser(lst):
    original_list = []
    for i in range(0, len(lst), 2):
        count = lst[i]
        value = lst[i + 1]
        original_list.extend([value] * count)
    
    return original_list

# problem 4
# TODO: saves everything as str instead of 'correct' format
def comma_separated_columns(filename):
    with open(filename, 'r', encoding='utf-8-sig') as file:
        lines = file.readlines()

    headers = lines[0].strip().split(',')

    data = {header: [] for header in headers}

    for line in lines[1:]:
        values = line.strip().split(',')
        for i, value in enumerate(values):
            header = headers[i]
            data[header].append(value)

    result = [(header, data[header]) for header in headers]

    return result

# problem 5
def bubble_sort(lst):
    n = len(lst)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    
    return lst