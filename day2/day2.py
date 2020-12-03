import re;

lines = None;
valid = 0;

pattern = re.compile('^(?P<min>\d+)-(?P<max>\d+) (?P<req>[a-z]): (?P<pass>\w*)$')
with open('day2input.txt', 'r') as input:
    lines = input.readlines();

for line in lines:
    match = pattern.match(line)
    print(match)
    _min = int(match.group('min'))
    _max = int(match.group('max'))
    _req = match.group('req')
    _pass = match.group('pass')
    print(_min, _max, _req, _pass)



    # count = 0
    # for char in _pass:
    #     print(char)
    #     if char == _req:
    #         count += 1
    # print(count)
    if (_pass[_min-1] == _req and _req != _pass[_max-1]) or (_pass[_min-1] != _req and _req == _pass[_max-1]):
        valid += 1
        print("valid")
    else:
        print("invalid")
print(valid)
    