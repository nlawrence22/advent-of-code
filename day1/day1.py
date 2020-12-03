input = []

with open('day1input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        input.append(int(line.strip()))
    print(input)


for index in range(0, len(input)):
    item = input[index]
    for i in range(index + 1, len(input)):
        compare = input[i]

        for j in range(i + 1, len(input)):
            third = input[j]

            if item + compare + third == 2020:
                print("Items: {item}, {compare}, {third}".format(item=item, compare=compare, third=third))
                print("Multiplied: {product}".format(product=item*compare*third))
