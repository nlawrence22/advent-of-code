import re

lines = None
with open('input.txt', 'r') as file:
    lines = file.readlines()

"""
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

{
    'light red': [('1', 'bright white'), ('2', 'muted yellow')], 
    'dark orange': [('3', 'bright white'), ('4', 'muted yellow')], 
    'bright white': [('1', 'shiny gold')], 
    'muted yellow': [('2', 'shiny gold'), ('9', 'faded blue')], 
    'shiny gold': [('1', 'dark olive'), ('2', 'vibrant plum')], 
    'dark olive': [('3', 'faded blue'), ('4', 'dotted black')], 
    'vibrant plum': [('5', 'faded blue'), ('6', 'dotted black')], 
    'faded blue': None, 
    'dotted black': None
}

RULE_RE = re.compile('^(?P<num>\d+)\s(?P<type>[\w\s]+)\sbag.*$')
def parse_rules(lines):
    rules = {}

    for line in lines:
        #print(line)
        first = line.split(' bags contain ')
        #print(first)
        key = first[0].split('bags')[0]
        #print(key)
        first_rules = first[1].rstrip()
        #print(first_rules)

        if first_rules == 'no other bags.':
            #print('rule is none')
            rules[key] = None
        else:
            all_rules = []
            rule_list = first_rules.split(', ')
            #print(rule_list)
            for rule in rule_list:
                #print(rule)
                matches = RULE_RE.match(rule)
                #print(matches)
                num = matches.group('num')
                #print(num)
                bag_type = matches.group('type')
                #print(bag_type)
                all_rules.append((num, bag_type))
            #print(all_rules)
            rules[key] = all_rules
    return rules


def can_has_shiny_bag(bag_type, rules):
    #print('parsing bag ', bag_type)
    if bag_type == 'shiny gold':
        #print('returning true')
        return True
    else:
        this_bags_rules = rules[bag_type]
        #print('this bags rules ', this_bags_rules)
        if this_bags_rules is None:
            #print('no rules for this bag')
            return False
        
        for rule in this_bags_rules:
            #print('parsing rule ', rule)
            num, bag_type = rule
            if can_has_shiny_bag(bag_type, rules):
                return True
        #print('no bags in this bag can has gold')
        return False
                



def count_bags(bag_type, rules):
    print('checking bag type', bag_type)
    rule_set = rules[bag_type]
    print(bag_type, ' has ruleset ', rule_set)
    if rule_set is None:
        print(bag_type, ' contains 0 bags')
        print('exiting ', bag_type)
        return 0
    else:
        count = 0
        for (num, bag_type_rule) in rule_set:
            print('doing rule ', num, bag_type_rule)
            bags_within = count_bags(bag_type_rule, rules)
            if bags_within == 0:
                print('no bags within')
                count += int(num, 10)
            else:
                increase = int(num, 10) + (int(num, 10) * bags_within)
                print('adding ', increase, ' bags for contained type ', bag_type_rule)
                count += increase
            print('count now ', count)

        print(bag_type, ' contains ', count, ' bags ')
        print('exiting ', bag_type)
        return count
    


rules = parse_rules(lines)

# print(rules)

# total = 0

# for bag_type, rule_set in rules.items():
#     #print('doing ', bag_type)
#     can_contain_gold = False

#     if rule_set is None:
#         continue

#     for num, bag_type in rules[bag_type]:
#         if can_has_shiny_bag(bag_type, rules):
#             can_contain_gold = True
#             break
    
#     if can_contain_gold:
#         total += 1
    

total_bags = 0
for rule in rules['shiny gold']:
    print('rule ', rule)
    num, bag_type = rule
    print(num, bag_type)
    bags_within = count_bags(bag_type, rules)
    print(bags_within)
    total_bags += int(num) + (int(num, 10) * bags_within)
    print('total now ', total_bags)
print(total_bags)