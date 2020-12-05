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
    mid = ((len(_list) - 1) // 2)
    if char == ROW_LOWER or char == COLUMN_LOWER:
        return _list[:bisect.bisect(_list, _list[mid])]
    elif char == ROW_UPPER or char == COLUMN_UPPER:
        return _list[bisect.bisect(_list, _list[mid]):]

for ticket in boarding_passes:
    row = None
    row_val = ticket[:7]
    col = None
    col_val = ticket[7:]

    row_list = rows[:]
    for char in row_val:
        row_list = binarySearch(row_list, char)
    row = row_list[0]

    col_list = columns[:]
    for char in col_val.strip():
        col_list = binarySearch(col_list, char)
    col = col_list[0]

    _id = row * 8 + col
    seats.append(_id)

seats.sort()

for index, seat in enumerate(seats):
    if index < 1:
        continue
    
    if seats[index - 1] != seat - 1:
        print('Found seat! Id: ', seat - 1)
        break

    elif seats[index + 1] != seat + 1:
        print('Found seat! Id: ', seat + 1)
        break
