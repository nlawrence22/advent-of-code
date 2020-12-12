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

def get_dir_from_heading(current_dir):
    direction = None

    if current_dir == NORTH_DIR:
        direction = NORTH
    elif current_dir == EAST_DIR:
        direction = EAST
    elif current_dir == SOUTH_DIR:
        direction = SOUTH
    elif current_dir == WEST_DIR:
        direction = WEST
    else:
        raise Exception('Unknown heading')

    return direction

def move_forward(current_dir, units, current_x, current_y):
    heading = get_dir_from_heading(current_dir)
    return move_in_dir(heading, units, current_x, current_y)

def get_new_heading(current_dir, direction, units):
    print('getting new heading!')
    print('current heading = {}, instruction= {}, {}'.format(current_dir, direction, units))
    value = current_dir

    if direction is LEFT:
        value = current_dir - units
    elif direction is RIGHT:
        value = current_dir + units

    if value < 0:
        return value + 360
    elif value > 360:
        return value - 360
    elif value == 360:
        return 0
    else:
        return value

def move_ship(direction, units, current_x, current_y, current_dir):
    new_x = current_x
    new_y = current_y
    new_dir = current_dir

    if direction is NORTH or direction is EAST or direction is SOUTH or direction is WEST:
        new_x, new_y = move_in_dir(direction, units, current_x, current_y)
    elif direction is FORWARD:
        new_x, new_y =  move_forward(current_dir, units, current_x, current_y)
    elif direction is LEFT or direction is RIGHT:
        new_dir = get_new_heading(current_dir, direction, units)
    else:
        raise Exception('Unknown instruction')

    return new_x, new_y, new_dir

def calc_manhattan_distance(current_x, current_y):
    return abs(current_x) + abs(current_y)


facing_dir = EAST_DIR
x_pos = 0
y_pos = 0
# print('x={}, y={}, heading={}'.format(x_pos, y_pos, facing_dir))
for direction, units in get_direction_input('input.txt'):
    # print('instruction=', direction, units)
    x_pos, y_pos, facing_dir = move_ship(direction, units, x_pos, y_pos, facing_dir)
    # print('x={}, y={}, heading={}'.format(x_pos, y_pos, facing_dir))

print(calc_manhattan_distance(x_pos, y_pos)) 


