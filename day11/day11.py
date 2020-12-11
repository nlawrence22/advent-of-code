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
def get_left_dir(x, y):
    new_x = x-1
    while new_x >= 0 and layout[y][new_x] is FLOOR :
        new_x -= 1

    if not new_x >= 0:
        return None
    elif layout[y][new_x] is not FLOOR:
        return (new_x, y)
    else:
        return None

@cache
def get_right_dir(x, y):
    new_x = x+1
    while new_x < width and layout[y][new_x] is FLOOR:
        new_x += 1

    if not new_x < width:
        return None
    elif layout[y][new_x] is not FLOOR:
        return (new_x, y)
    else:
        return None

@cache
def get_nw_dir(x,y):
    new_x = x-1
    new_y = y-1
    while new_x >= 0 and new_y >= 0 and layout[new_y][new_x] is FLOOR:
        new_x -= 1
        new_y -= 1

    if not new_x >= 0 or not new_y >= 0:
        return None
    elif layout[new_y][new_x] is not FLOOR:
        return (new_x, new_y)
    else:
        return None

@cache
def get_sw_dir(x,y):
    new_x = x-1
    new_y = y+1
    while new_x >= 0 and new_y < height and layout[new_y][new_x] is FLOOR:
        new_x -= 1
        new_y += 1

    if not new_x >= 0 or not new_y < height:
        return None
    elif layout[new_y][new_x] is not FLOOR:
        return (new_x, new_y)
    else:
        return None

@cache
def get_ne_dir(x,y):
    new_x = x+1
    new_y = y-1
    while new_x < width and new_y >= 0 and layout[new_y][new_x] is FLOOR:
        new_x += 1
        new_y -= 1

    if not new_x < width or not new_y >= 0:
        return None
    elif layout[new_y][new_x] is not FLOOR:
        return (new_x, new_y)
    else:
        return None

@cache
def get_se_dir(x,y):
    new_x = x+1
    new_y = y+1
    while new_x < width and new_y < height and layout[new_y][new_x] is FLOOR:
        new_x += 1
        new_y += 1

    if not new_x < width or not new_y < height:
        return None
    elif layout[new_y][new_x] is not FLOOR:
        return (new_x, new_y)
    else:
        return None

@cache
def get_up_dir(x, y):
    new_y = y-1
    while new_y >= 0 and layout[new_y][x] is FLOOR:
        new_y -= 1

    if not new_y >= 0:
        return None
    elif layout[new_y][x] is not FLOOR:
        return (x, new_y)
    else:
        return None

@cache
def get_down_dir(x, y):
    new_y = y+1
    while new_y < height and layout[new_y][x] is FLOOR:
        new_y += 1

    if not new_y < height:
        return None
    elif layout[new_y][x] is not FLOOR:
        return (x, new_y)
    else:
        return None

def get_neighboring_coords(x, y):
    neighbors = []

    # seat x-1, y
    if not (x - 1) < 0:
        left_dir = get_left_dir(x, y)
        if left_dir is not None:
            neighbors.append(left_dir)
        # seat x-1, y-1
        if not (y - 1) < 0:
            nw_dir = get_nw_dir(x, y)
            if nw_dir is not None:
                neighbors.append(nw_dir)
        # seat x-1, y+1
        if not (y + 1) >= height:
            sw_dir = get_sw_dir(x, y)
            if sw_dir is not None:
                neighbors.append(sw_dir)
    # seat x+1, y
    if not (x + 1) >= width:
        right_dir = get_right_dir(x,y)
        if right_dir is not None:
            neighbors.append(right_dir)
        # seat x+1, y-1
        if not (y - 1) < 0:
            ne_dir = get_ne_dir(x,y)
            if ne_dir is not None:
                neighbors.append(ne_dir)
        # seat x+1, y+1
        if not (y + 1) >= height:
            se_dir = get_se_dir(x,y)
            if se_dir is not None:
                neighbors.append(se_dir)
                
    # seat i, j+1
    if not (y+1) >= height:
        down_dir = get_down_dir(x,y)
        if down_dir is not None:
            neighbors.append(down_dir)

    # seat i, j-1
    if not (y-1) < 0:
        up_dir = get_up_dir(x,y)
        if up_dir is not None:
            neighbors.append(up_dir)

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

            if seat is FULL and number_of_neighbors < 5:
                # skip this too, can't change to empty unless 4+ are occupied
                new_row.append(seat)
                continue

            full_neighbors = 0
            for i,j in get_neighboring_coords(x, y):
                old_seat = old_layout[j][i]
                if old_seat is FULL:
                    full_neighbors += 1
                if full_neighbors >= 5:
                    break
            
            if seat is EMPTY and full_neighbors == 0:
                new_row.append(FULL)
            elif seat is FULL and full_neighbors >= 5:
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

        if old_data != new_data:
            equal = False
            break
    
    return equal

# def print_layout(representation):
#     for row in representation:
#       print(''.join(row))

old_layout = layout
new_layout = shuffle_people(layout)

rounds = 0
isEqual = False
while isEqual is False:
    # print('round', rounds)
    # print_layout(old_layout)
    # print('')
    # print_layout(new_layout)
    old_layout = new_layout
    new_layout = shuffle_people(old_layout)

    isEqual = are_layouts_equal(old_layout, new_layout)
    # print('isEqual', isEqual, '\n')
    rounds += 1

def count_occupied_seats(layout):
    count = 0
    for row in layout:
        for seat in row:
            if seat is FULL:
                count += 1
    return count

print(count_occupied_seats(new_layout))
