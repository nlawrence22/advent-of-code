numbers = None
with open('input.txt', 'r') as file:
    numbers = file.readlines()

def is_valid_next_num(this_num, data, first_window_idx, last_window_idx):
    isValid = False
    for idx in range(first_window_idx, last_window_idx):
        for second_idx in range(first_window_idx, last_window_idx):
            if idx == second_idx:
                continue

            result = int(data[idx].rstrip(), 10) + int(data[second_idx].rstrip(), 10)
            if this_num == result:
                isValid = True
                break
        
        if isValid is True:
            break
    
    return isValid
    
def find_weakness(data, window):
    first_idx = 0
    last_idx = window

    this_num = int(data[last_idx])
    weaknessFound = False
    for i in range(window, len(data)):
        result = is_valid_next_num(this_num, data, first_idx, last_idx)

        if result is False:
            weaknessFound = True
            break

        first_idx += 1
        last_idx += 1
        this_num = int(data[last_idx].strip(), 10)
    
    if weaknessFound:
        return int(data[last_idx].strip(), 10)
    else:
        print('no weakness found!')

weakness = find_weakness(numbers, 25)
print('found weakness ', weakness)

def find_min_max(data, num_to_sum):
    start = 0
    minimum = start
    maximum = None

    while maximum is None:
        maximum = find_max(minimum, num_to_sum, data)
        if maximum is None:
            minimum += 1
    
    return minimum, maximum

def find_max(start, num_to_sum, data):
    #print('finding max starting at ', start)
    cursor = start
    total = 0
    success = False
    for num in data[start:]:
        total += int(data[cursor].strip(), 10)
        if total > num_to_sum:
            break
        elif total == num_to_sum:
            print('total ', total)
            success = True
            break
        cursor += 1

    if success == True:
        return cursor
    else:
        return None

minimum, maximum = find_min_max(numbers, weakness)

nums = []
for i in range(minimum, maximum+1):
    nums.append(int(numbers[i].strip(), 10))
    print(nums)

print('min=', minimum, 'max=', maximum)
nums.sort()
print('nums', nums)
print(max(nums), min(nums))
answer = max(nums) + min(nums)

print(answer)
            