# --- Day day05 ---
#    _____                   __         _____ __             __       
#   / ___/__  ______  ____  / /_  __   / ___// /_____ ______/ /_______
#   \__ \/ / / / __ \/ __ \/ / / / /   \__ \/ __/ __ `/ ___/ //_/ ___/
#  ___/ / /_/ / /_/ / /_/ / / /_/ /   ___/ / /_/ /_/ / /__/ ,< (__  ) 
# /____/\__,_/ .___/ .___/_/\__, /   /____/\__/\__,_/\___/_/|_/____/  
#           /_/   /_/      /____/                                     
# 
import queue


def load_input(filename):
    lines = []
    with open(filename) as f:
        lines = f.readlines()
    
    stacks = []
    for line in lines:
        if "1" in line:
            break

        x = line.replace("[", " ").replace("]", " ").replace("\n", "")
        stacks.append(x)
        print(x)

    return lines


def part1(input):
    stacks = []
    # for 


def part2(input):
    pass


if __name__ == "__main__":
    input = load_input('day05/input_simple.txt')
    # input = load_input('day05/input.txt')

    part1(input)
    # part2(input)
