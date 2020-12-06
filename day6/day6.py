
lines = None
with open('input.txt', 'r') as file:
    lines = file.readlines()

lines = "".join(lines)

groups = lines.split('\n\n')

totals = []

# for group in groups:
#     unique = set()
#     for char in group:
#         if char == '\n':
#             continue
#         unique.add(char)
#     print(unique, len(unique))
#     totals.append(len(unique))

for group in groups:
    print('group ', group)
    answers = group.split('\n')
    sets = []
    for answer in answers:
        new = set()
        for char in answer:
            if char == '\n':
                continue
            new.add(char)
        sets.append(new)

    print('answers ', answers)
    print('sets', sets)
    if (len(sets) > 1):
        intersection = sets[0].intersection(*sets)
    elif (len(sets) == 0):
        intersection = []
    else:
        intersection = sets[0]

    print('intersection', intersection)
    totals.append(len(intersection))

print(sum(totals))


with open('input.txt', 'r') as file:
    lines = file.readlines()