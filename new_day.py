import os, sys

solution_template = """# --- Day {{DAYNO}} ---

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


def load_input(filename):
    with open(filename) as f:
        return f.readlines()


def part1(input):
    pass


def part2(input):
    pass


if __name__ == "__main__":
    input = load_input('day{{DAYNO}}/day{{DAYNO}}_input.txt')

    part1(input)
    # part2(input)
"""


if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        raise RuntimeError(f'Expected 1 integer argument for the day number. Found {len(sys.argv) - 1}')

    try: 
        day_no = int(sys.argv[1])

    except ValueError:
        raise RuntimeError(f'Input could not be converted to integer. Try again.')

    # create the directory for the day's challenge
    aoc_dir = os.path.dirname(os.path.abspath(__file__))
    day_dir = os.path.join(aoc_dir, f'day{day_no}')
    print(day_dir)
    os.mkdir(day_dir)

    # create the solution file with the template code
    solution_filename = os.path.join(day_dir, f'day{day_no}_solution.py')
    with open(solution_filename, 'w') as f:
        f.writelines(solution_template.replace('{{DAYNO}}', str(day_no)))

    # create the empty input files
    input_filename1 = os.path.join(day_dir, f'day{day_no}_input.txt')
    input_filename2 = os.path.join(day_dir, f'day{day_no}_input_simple.txt')
    open(input_filename1, 'w')
    open(input_filename2, 'w')