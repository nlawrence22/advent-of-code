import re

validFields = {
    "byr": 1,
    "iyr": 1,
    "eyr": 1,
    "hgt": 1,
    "hcl": 1,
    "ecl": 1,
    "pid": 1
}

valid = 0

lines = None
with open('day4input.txt', 'r') as input:
    lines = input.readlines();

#print(lines)
def getPassports(input):
    passports = []
    passport = {}
    for line in input:
        #print(line)
        if line == '\n':
            #print('passport', passport)
            #print('end of passport')
            passports.append(passport)
            passport = {}
            continue
        else:
            fields = line.split(' ')
            #print('fields', fields)
            for field in fields:
                field_data = field.split(':')
                #print('field data', field_data)
                passport[field_data[0]] = field_data[1].strip()
            #print('passport', passport)

    #print('passport', passport)
    passports.append(passport)
    return passports

passports = getPassports(lines)

def isValidByr(value):
    try:
        num = int(value)
        if 1920 <= num and num <= 2002:
            return True
        else:
            return False
    except:
        return False

def isValidIyr(value):
    try:
        num = int(value)
        if 2010 <= num and num <= 2020:
            return True
        else:
            return False
    except:
        return False 

def isValidEyr(value):
    try:
        num = int(value)
        if 2020 <= num and num <= 2030:
            return True
        else:
            return False
    except:
        return False  


HEIGHT_RE = re.compile('^(?P<num>\d+)(?P<unit>in|cm)$')
def isValidHgt(value):
    matches = HEIGHT_RE.match(value)
    if matches == None:
        return False
    
    value = matches.group('num')
    unit = matches.group('unit')

    try:
        value = int(value)
    except:
        return False

    if unit == 'in':
        if 59 <= value and value <= 76:
            return True
        else:
            return False
    elif unit == 'cm':
        if 150 <= value and value <= 193:
            return True
        else:
            return False
    else:
        return False

HAIR_RE = re.compile('^#[0-9a-f]{6}$')
def isValidHcl(value):
    match = HAIR_RE.match(value)

    if match != None:
        return True
    else:
        return False

def isValidEcl(value):
    if value == 'amb' or value == 'blu' or value == 'brn' or value == 'gry' or value == 'grn' or value == 'hzl' or value == 'oth':
        return True
    else:
        return False

def isValidPid(value):
    if len(value) != 9:
        return False
    
    try:
        int(value)
        return True
    except:
        return False


def fieldValidator(type, value):
    if type == 'byr':
        return isValidByr(value)
    elif type == 'iyr':
        return isValidIyr(value)
    elif type == 'eyr':
        return isValidEyr(value)
    elif type == 'hgt':
        return isValidHgt(value)
    elif type == 'hcl':
        return isValidHcl(value)
    elif type == 'ecl':
        return isValidEcl(value)
    elif type == 'pid':
        return isValidPid(value)
    elif type == 'cid':
        return True
    else:
        return False

for passport in passports:
    isValid = True
    for field in dict.keys(validFields):
        if passport.get(field) == None:
            print("passport", passport)
            print('missing', field)
            isValid = False
            break

    if not isValid:
        continue

    for key, value in passport.items():
        if fieldValidator(key, value) == False:
            print('field ', key, ' invalid value ', value)
            isValid = False
            break;
    
    if isValid:
        valid +=1

print(valid)