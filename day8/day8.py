
original_program_code = None
with open('input.txt', 'r') as file:
    original_program_code = file.readlines()

accumulator = 0

def runProgram(program_code):
    accumulator = 0
    seen_instructions = set()

    next_instruction = program_code[0]
    index = 0
    seen_instructions.add(index)

    while True:
        last_instruction = index
        this_instruction = next_instruction.split(' ')
        op = this_instruction[0]
        val = this_instruction[1].rstrip()

        if op == 'acc':
            accumulator += int(val, 10)
            index += 1
        elif op == 'nop':
            index += 1
        elif op == 'jmp':
            index += int(val, 10)
        
        if index in seen_instructions:
            print('loop detected')
            return False
        elif index < 0:
            print('erroneous jump detected at instruction: {}'.format(last_instruction))
            return False
        elif index > len(program_code) - 1:
            print('end of instructions reached')
            return accumulator

        seen_instructions.add(index)
        next_instruction = program_code[index]
        this_instruction = None

def get_num_ops():
    jump_idx_list = []
    no_op_idx_list = []
    print(original_program_code)
    for index, op in enumerate(original_program_code):
        # print(index, op)
        action = op.split(' ')[0]
        # print(action)
        if action == 'jmp':
            jump_idx_list.append(index)
        elif action == 'nop':
            no_op_idx_list.append(index)

    return jump_idx_list, no_op_idx_list

was_successful = False
jump_idx_list, no_op_idx_list = get_num_ops()
jumps_changed = set()
nops_changed = set()

new_code = None
for idx in jump_idx_list:
    print('changing jump at ', idx)
    new_code = original_program_code.copy()
    instruction_to_change = original_program_code.copy()[idx].split(' ')
    new_code[idx] = 'nop {}'.format(instruction_to_change[1])

    result = runProgram(new_code)
        
    if result is not False:
        print('success')
        was_successful = result
        break
    

if was_successful is False:
    print('All Jumps Modified, trying nop modifications')

    for idx in no_op_idx_list:
        print('changing nop at ', idx)
        new_code = original_program_code.copy()
        instruction_to_change = original_program_code.copy()[idx].split(' ')
        new_code[idx] = 'nop {}'.format(instruction_to_change[1])

        print('new code:\n', new_code)
        result = runProgram(new_code)
        print(result)

        if result is None:
            print('success!')
            was_successful = result
            break


print(was_successful)