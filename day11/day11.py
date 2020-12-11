from functools import cache

def get_seating_layout(filename):
    seating_layout = []
    with open(filename, 'r') as file:
        for line in file:
            seating_row = []
            for char in line.rstrip():
                seating_row.append(char)
            seating_layout.append(seating_row)
    
    return seating_layout

layout = get_seating_layout('input.txt')

width = len(layout[0])
height = len(layout)

@cache
def get_neighboring_coords(x, y):
    neighbors = []

    # seat x-1, y
    if not (x - 1) < 0:
        neighbors.append((x-1, y))
        # seat x-1, y-1
        if not (y - 1) < 0:
            neighbors.append((x-1, y-1))
        # seat x-1, y+1
        if not (y + 1) >= height:
            neighbors.append((x-1, y+1))
    # seat x+1, y
    if not (x + 1) >= width:
        neighbors.append((x+1, y))
        # seat x+1, y-1
        if not (y - 1) < 0:
            neighbors.append((x+1, y-1))
        # seat x+1, y+1
        if not (y + 1) >= height:
            neighbors.append((x+1, y+1))
                
    # seat i, j+1
    if not (y+1) >= height:
        neighbors.append((x, y+1))

    # seat i, j-1
    if not (y-1) < 0:
        neighbors.append((x, y-1))

    return neighbors     

FULL = '#'
EMPTY = 'L'
FLOOR = '.'

def shuffle_people(layout):
    old_layout = layout.copy()
    new_layout = []
    for y, row in enumerate(old_layout):
        new_row = []
        for x, seat in enumerate(row):
            # seat x, y <- WE ARE HERE
            if seat is FLOOR:
                # skip floors, these are constant
                new_row.append(seat)
                continue

            neighbors = get_neighboring_coords(x, y)
            number_of_neighbors = len(neighbors)

            """
            If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
            If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
            Otherwise, the seat's state does not change.
            """

            if seat is FULL and number_of_neighbors < 4:
                # skip this too, can't change to empty unless 4+ are occupied
                new_row.append(seat)
                continue

            full_neighbors = 0
            for i,j in get_neighboring_coords(x, y):
                #print('getting old x={}, y={}, width={}, height={}'.format(i, j, width, height))
                old_seat = old_layout[j][i]
                if old_seat is FULL:
                    full_neighbors += 1
                if full_neighbors >= 4:
                    break
            
            if seat is EMPTY and full_neighbors == 0:
                new_row.append(FULL)
            elif seat is FULL and full_neighbors >= 4:
                new_row.append(EMPTY)
            else:
                new_row.append(seat)
        
        new_layout.append(new_row)
    
    return new_layout

def are_layouts_equal(old, new):
    equal = True
    for index, row in enumerate(old):
        old_data = ''.join(row)
        new_data = ''.join(new[index])

        #print('index {}: oldrow={}, newRow={}'.format(index, old_data, new_data))
        if old_data != new_data:
            #print('not equal!')
            equal = False
            break
    
    return equal

old_layout = layout
new_layout = shuffle_people(layout)

rounds = 0
isEqual = False
while isEqual is False:
    #print('round', rounds)
    old_layout = new_layout
    new_layout = shuffle_people(old_layout)

    isEqual = are_layouts_equal(old_layout, new_layout)
    #print('isEqual', isEqual)
    rounds += 1

def count_occupied_seats(layout):
    count = 0
    for row in layout:
        for seat in row:
            if seat is FULL:
                count += 1
    return count

print(count_occupied_seats(new_layout))


# for row in new_layout:
#     print(''.join(row))

# print('')
# print('')

# third_layout = shuffle_people(new_layout)

# for row in third_layout:
#     print(''.join(row))