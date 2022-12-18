# --- Day 05 ---
#    _____                   __         _____ __             __       
#   / ___/__  ______  ____  / /_  __   / ___// /_____ ______/ /_______
#   \__ \/ / / / __ \/ __ \/ / / / /   \__ \/ __/ __ `/ ___/ //_/ ___/
#  ___/ / /_/ / /_/ / /_/ / / /_/ /   ___/ / /_/ /_/ / /__/ ,< (__  ) 
# /____/\__,_/ .___/ .___/_/\__, /   /____/\__/\__,_/\___/_/|_/____/  
#           /_/   /_/      /____/                                     
# 

class Stack():
    def __init__(self) -> None:
        self.data = []

    def get(self): 
        return self.data.pop(-1)

    def put(self, value):
        return self.data.append(value)

    def has_value(self):
        return len(self.data) > 0

    def reverse(self):
        self.data = self.data[::-1]


def print_stacks(stacks: list[Stack]):
    for x in stacks:
        print(x.data)


def load_input(filename):
    lines = []
    with open(filename) as f:
        lines = f.readlines()
    
    stacks: list[Stack] = []
    stack_count = int(len(lines[0]) / 4)
    for i in range(0, stack_count):
        stacks.append(Stack())

    # preprocess to remove uneeded characters
    index = 0
    while True:
        line = lines[index]
        index += 1
        if "1" in line:
            break

        count = 0
        for i in range(1, len(lines[0]), 4):
            if line[i] != ' ':
                stacks[count].put(line[i])
            count += 1
    
    for i in range(0, stack_count):
        stacks[i].reverse()

    instructions = []
    while True:
        index += 1
        try:
            line = lines[index].strip()
        except IndexError:
            break
        instructions.append(line.split(" ")[1::2])

    return stacks, instructions


def part1(stacks: list[Stack], instructions: list[list[str]]):
    for instruction in instructions:
        move = int(instruction[0])
        start = int(instruction[1]) - 1
        end = int(instruction[2]) - 1

        for _ in range(0, move):
            stacks[end].put(stacks[start].get())

    output = ''
    for stack in stacks:
        output+= stack.data[-1]
    print(output)


def part2(stacks: list[Stack], instructions: list[list[str]]):
    for instruction in instructions:
        move = int(instruction[0])
        start = int(instruction[1]) - 1
        end = int(instruction[2]) - 1
        
        temp_stack = Stack()
        for _ in range(0, move):
            temp_stack.put(stacks[start].get())
        for _ in range(0, move): 
            stacks[end].put(temp_stack.get())

    output = ''
    for stack in stacks:
        output += stack.data[-1]
    print(output)


if __name__ == "__main__":
    print(__file__)
    dir = '/'.join(__file__.split('/')[:-1])
    stacks, instructions = load_input(dir + '/input_simple.txt')
    stacks, instructions = load_input(dir + '/input.txt')

    # part1(stacks, instructions)
    part2(stacks, instructions)
