import bisect

rows = range(128)
columns = range(8)

ROW_LOWER = 'F'
ROW_UPPER = 'B'

COLUMN_LOWER = 'L'
COLUMN_UPPER = 'R'

boarding_passes = []
seats = []

with open('day5input.txt', 'r') as file:
    for line in file:
        boarding_passes.append(line)

def binarySearch(_list, char):
    #print('doing binary search')
    mid = ((len(_list) - 1) // 2)
    #print('value = ', _list[mid])
    if char == ROW_LOWER or char == COLUMN_LOWER:
        #print('new end ', _list[mid])
        return _list[:bisect.bisect(_list, _list[mid])]
    elif char == ROW_UPPER or char == COLUMN_UPPER:
        #print('new start ', _list[mid])
        return _list[bisect.bisect(_list, _list[mid]):]

for ticket in boarding_passes:
    row = None
    row_val = ticket[:7]
    col = None
    col_val = ticket[7:]

    row_list = rows[:]
    for char in row_val:
        #print('rows: ', row_list[0], ' to ', row_list[len(row_list)-1])
        #print('Finding value for ', char)
        row_list = binarySearch(row_list, char)
        #print('New list: ', row_list)
    row = row_list[0]
    #print('row found: ', row)

    col_list = columns[:]
    iteration = 0
    for char in col_val.strip():
        #print('iteration: ', iteration + 1)
        iteration +=1
        #print('cols: ', col_list[0], ' to ', col_list[len(col_list) -1])
        #print('Finding value for ', char)
        col_list = binarySearch(col_list, char)
        #print('new list: ', col_list)
    col = col_list[0]
    #print('col found: ', col)

    _id = row * 8 + col
    #print('id: ', _id)
    seats.append(_id)

#print('max: ', max_id)

seats.sort()
#print('seats', seats)

for index, seat in enumerate(seats):
    #print('inspecting seat ', seat)
    if index < 1:
        continue
    
    #print('seat left ', seats[index - 1], ' seat right ', seats[index + 1])
    if seats[index - 1] != seat - 1 or seats[index + 1] != seat + 1:
        print('Found seat! Id: ', seat + 1)
        break






