
trees = 0
TREE = '#'

lines = None
with open('day3input.txt', 'r') as input:
    lines = input.readlines();

rows = len(lines)
columns = len(lines[0])

# total_needed_columns = 3 * rows;

# columns = 0
# while columns < total_needed_columns:
#     for index, line in enumerate(lines):
#         lines[index] = line.strip() + line.strip()
#         columns += len(lines[index])

# print('\n'.join(lines))
# print("{}, {}, {}", rows, initial_columns, columns)

# column_cursor = 0
# for line in lines:
#     print("before", column_cursor)
#     if column_cursor > len(line) - 1:
#         column_cursor = abs(column_cursor - (len(line) - 1))
#         print("after", column_cursor)

#     print(line)
#     if line[column_cursor] == TREE:
#         print(line[column_cursor], " is tree!")
#         trees += 1
#     column_cursor += 3

column = 0
for line in lines:
    if line[column % (len(line) - 1)] == TREE:
        trees += 1
    column +=3

print(trees)


# PART TWO #

"""
    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.
"""


paths = [
    (1,1),
    (3,1),
    (5,1),
    (7,1),
    (1,2)
]

def findTrees (path):
    _trees = 0
    right, down = path
    print("Path", path)
    # print("right", right)
    # print("down", down)

    col = right
    for i in range(down, len(lines), down):
        row = i
        width = len(lines[row]) -1

        if lines[row][(col % width)] == TREE:
            _trees += 1
        
        col += right
    
    print("trees", _trees)
    return _trees

results = []
for path in paths:
    results.append(findTrees(path))

product = 1
for num in results:
    product *= num

print(product)
# print(rows)