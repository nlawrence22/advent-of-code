NORTH_DIR = 0
EAST_DIR = 90
SOUTH_DIR = 180
WEST_DIR = 270

LEFT = 'L'
RIGHT = 'R'
FORWARD = 'F'
NORTH = 'N'
SOUTH = 'S'
EAST = 'E'
WEST = 'W'


def get_direction_input(filename):
    directions = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.rstrip()
            direction = line[0]
            units = int(line[1:], 10)
            directions.append((direction, units))

    return directions

def move_north(units, current_x, current_y):
    return current_x, current_y + units

def move_east(units, current_x, current_y):
    return current_x + units, current_y

def move_south(units, current_x, current_y):
    return current_x, current_y - units

def move_west(units, current_x, current_y):
    return current_x - units, current_y

def move_in_dir(direction, units, current_x, current_y):
    new_x = current_x
    new_y = current_y

    if direction is NORTH:
        new_x, new_y = move_north(units, current_x, current_y)
    elif direction is EAST:
        new_x, new_y = move_east(units, current_x, current_y)
    elif direction is SOUTH:
        new_x, new_y = move_south(units, current_x, current_y)
    elif direction is WEST:
        new_x, new_y = move_west(units, current_x, current_y)

    return new_x, new_y

# def get_dir_from_heading(current_dir):
#     direction = None

#     if current_dir == NORTH_DIR:
#         direction = NORTH
#     elif current_dir == EAST_DIR:
#         direction = EAST
#     elif current_dir == SOUTH_DIR:
#         direction = SOUTH
#     elif current_dir == WEST_DIR:
#         direction = WEST
#     else:
#         raise Exception('Unknown heading')

#     return direction

def move_forward(units, waypoint_x, waypoint_y, current_x, current_y):
    new_x = current_x
    new_y = current_y
    x_change = waypoint_x
    y_change = waypoint_y

    if waypoint_x < 0:
        x_change = (-1 * abs(waypoint_x * units))
    else:
        x_change = (waypoint_x * units)
    
    if waypoint_y < 0:
        y_change = (-1 * abs(waypoint_y * units))
    else:
        y_change = (waypoint_y * units)
    
    return current_x + x_change, current_y + y_change

""" 
WXL
XSX
RXX

-1,1
L 1, 1
R -1, -1    

XLX
WSX
XRX

-1, 0
L 0, 1
R 0, -1

LXX
XSX
WXR

-1, -1
L -1, 1
R 1, -1 
"""

def rotate_waypoint(direction, units, waypoint_x, waypoint_y):
    new_x = waypoint_x
    new_y = waypoint_y

    if units == 180:
        new_x = -waypoint_x
        new_y = -waypoint_y
    elif units == 90:
        if direction is LEFT:
            new_x = -waypoint_y
            new_y = waypoint_x
        elif direction is RIGHT:
            new_x = waypoint_y
            new_y = -waypoint_x
    elif units == 270:
        if direction is LEFT:
            new_x = waypoint_y
            new_y = -waypoint_x
        elif direction is RIGHT:
            new_x = -waypoint_y
            new_y = waypoint_x

    return new_x, new_y

def move_waypoint(direction, units, current_x, current_y):
    new_x = current_x
    new_y = current_y

    if direction is NORTH or direction is EAST or direction is SOUTH or direction is WEST:
        new_x, new_y = move_in_dir(direction, units, current_x, current_y)
    elif direction is LEFT or direction is RIGHT:
        new_x, new_y = rotate_waypoint(direction, units, waypoint_x, waypoint_y)
    else:
        raise Exception('Unknown instruction')

    return new_x, new_y

def calc_manhattan_distance(current_x, current_y):
    return abs(current_x) + abs(current_y)

x_pos = 0
y_pos = 0
waypoint_x = 10
waypoint_y = 1

for direction, units in get_direction_input('input.txt'):
    print('instruction=', direction, units)
    if direction is FORWARD:
        x_pos, y_pos = move_forward(units, waypoint_x, waypoint_y, x_pos, y_pos)
    else:
        waypoint_x, waypoint_y = move_waypoint(direction, units, waypoint_x, waypoint_y)

print(calc_manhattan_distance(x_pos, y_pos)) 


