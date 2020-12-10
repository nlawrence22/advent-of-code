from collections import defaultdict
from functools import cache

def get_input_as_strings(filename):
    lines = None
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    return lines

def get_input_as_ints(filename):
    lines = get_input_as_strings(filename)
    new_lines = []

    for line in lines:
        if line == '\n':
            continue
        digit = int(line.rstrip(), 10)
        new_lines.append(digit)

    return new_lines

adapters = get_input_as_ints('input.txt')
adapters.sort()
# print(adapters)

starting_jolts = 0
if adapters[0] > starting_jolts + 3:
    raise Exception('cant connect!')

jolts = starting_jolts
diff_1 = 0
diff_3 = 1 # Final adapter counts
for adapter in adapters:
    # print('checking adapter {}'.format(adapter))
    if adapter - 3 > jolts:
        raise Exception('jolts too low!')
    elif adapter - 3 == jolts:
        diff_3 += 1
        jolts = adapter
    elif adapter - 1 == jolts:
        diff_1 += 1
        jolts = adapter
    else:
        raise Exception('diff not 1 or 3!')
    # print('new jolts = {}', jolts)

print('diff_1 {} * diff_3 {} = {}'.format(diff_1, diff_3, diff_1 * diff_3))
total_jolts = jolts
print('total_jolts = {}'.format(jolts))

def get_possible_next_adapters(jolts, adapter_list):
    # print('getting possible next adapters for {} output jolts'.format(jolts))
    possiblilites = []

    for adapter in adapter_list:
        # print('checking', adapter)
        if adapter - 1 == jolts or adapter - 2 == jolts or adapter - 3 == jolts:
            # print('{} is valid!'.format(adapter))
            possiblilites.append(adapter)
    
    return possiblilites

class Graph:
    def __init__(self, vertices):
        self.Vertices = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    @cache
    def get_paths(self, curr, destination):
        count = 0
        if curr == destination:
            return 1
        else:
            for i in self.graph[curr]:
                count += self.get_paths(i, destination)
        return count

    def get_all_paths(self, start, destination):

        return self.get_paths(start, destination)
        #return self.count


path_graph = Graph(adapters)
print('graph built')

jolts = 0
# print('adapters', adapters)
remaining_adapters = adapters.copy()
remaining_adapters.sort()
for adapter in adapters:
    possibilites = get_possible_next_adapters(jolts, remaining_adapters)
    # print('possible next adapters', possibilites)

    for jlts in possibilites:
        # print('{} can connect to {}'.format(jolts, jlts))
        path_graph.addEdge(jolts, jlts)
    
    jolts = adapter
    remaining_adapters.remove(adapter)

# print(path_graph.graph)
the_answer = path_graph.get_all_paths(0, total_jolts)
# for pt in the_answer:
#     print(pt)
print(the_answer)
