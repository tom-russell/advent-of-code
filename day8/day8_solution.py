# --- Day 8 ---
#   _    _                 _ _          _     _   _    _       _ _   _             
#  | |  | |               | | |        | |   | | | |  | |     | | | (_)            
#  | |__| | __ _ _ __   __| | |__   ___| | __| | | |__| | __ _| | |_ _ _ __   __ _ 
#  |  __  |/ _` | '_ \ / _` | '_ \ / _ \ |/ _` | |  __  |/ _` | | __| | '_ \ / _` |
#  | |  | | (_| | | | | (_| | | | |  __/ | (_| | | |  | | (_| | | |_| | | | | (_| |
#  |_|  |_|\__,_|_| |_|\__,_|_| |_|\___|_|\__,_| |_|  |_|\__,_|_|\__|_|_| |_|\__, |
#                                                                             __/ |
#                                                                            |___/ 

import os, sys, copy
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


def load_input(filename):
    with open(filename) as f:
        instructions = []
        
        for line in f:
            line_split = line.strip().split(' ')
            instructions.append([line_split[0], int(line_split[1])])

        return instructions


def part1(instructions):
    visited_indexes = set()
    current_index = 0
    accumulator = 0

    # loop over the instructions until we reach the end, or enter an infinite loop
    while current_index < len(instructions):
        # if the index has already been visited then we are about to enter a loop
        if current_index in visited_indexes:
            raise RuntimeError(f'About the enter an infinite loop. Acc value at this point: {accumulator}')

        visited_indexes.add(current_index)
        instr = instructions[current_index]

        # jump instruction moves the index by the argument value
        if instr[0] == 'jmp':
            current_index += instr[1]
            continue

        # accumulator instruction changes the accumulator by the argument value
        if instr[0] == 'acc':
            accumulator += instr[1]

        # no-op instructions do nothing!
        # if we didn't jump, then we move to the next sequential instruction
        current_index += 1

    print(f'Reached the end of the instructions - no loop encountered! Final acc value: {accumulator}')
    return current_index


def part2(instructions):
    # we can change any one jmp to a nop, or a nop to a jmp, to fix the infinite loop.
    # the correct behaviour is for the boot code to reach the max index + 1. 

    # loop over every instruction, and test modifying each jmp/nop instruction until we find a 
    # working solution that exits cleanly
    for index in range(0, len(instructions)):
        operation = instructions[index][0]

        # we can only modify jmp/nop instructions
        if operation == 'acc':
            continue

        # flip the instruction from jmp -> nop or vice versa
        instructions[index][0] = 'jmp' if operation == 'nop' else 'nop'

        try:
            # run the boot code to test this solution
            final_index = part1(instructions)

            # the exit index must be immediately above index of the last instruction for a valid solution
            if final_index == len(instructions):
                print(f'Solution found! index {index} was changed to {instructions[index][0]}.')
                return


        # if an error is raised then the solution is not correct
        except RuntimeError:
            pass

        # set the instruction back to the original value for the next run
        instructions[index][0] = operation
    
    print('All iterations tested - no fix was found :(')


if __name__ == "__main__":
    # instructions = load_input('day8/day8_input_simple.txt')
    instructions = load_input('day8/day8_input.txt')

    # part1(instructions)
    part2(instructions)
