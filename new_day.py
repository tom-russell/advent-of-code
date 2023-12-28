import os
import sys

from pyfiglet import figlet_format

solution_template = """# --- {{DAYNO}} ---
# {{ascii}}

def load_input(filename):
    lines = []
    with open(filename) as f:
        while x := f.readline():
            lines.append(x.strip())
    return lines


def part1(input):
    pass


def part2(input):
    pass


if __name__ == "__main__":
    dir = '/'.join(__file__.split('/')[:-1])
    input = load_input(dir + '/input_simple.txt')
    # input = load_input(dir + '/input.txt')

    part1(input)
    # part2(input)
"""


if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise RuntimeError(
            f"Expected 3 arguments - year, day_no and day_name. Found {len(sys.argv) - 1}"
        )

    try:
        aoc_year = str(sys.argv[1])
        day_no = f"day{str(int(sys.argv[2])).zfill(2)}"
        day_name = str(sys.argv[3])
    except ValueError:
        raise RuntimeError("Input could not be converted to integer. Try again.")

    # create the directory for the day's challenge
    aoc_dir = os.path.dirname(os.path.abspath(__file__))
    day_dir = os.path.join(aoc_dir, aoc_year, day_no)
    os.mkdir(day_dir)

    # create the solution file with the template code
    solution_filename = os.path.join(day_dir, f"{day_no}_solution.py")
    with open(solution_filename, "w") as f:
        figlet_output = figlet_format(font="slant", text=day_name)
        ascii = figlet_output.replace("\n", "\n# ")
        ascii = "\n".join(line.rstrip() for line in ascii.split("\n"))
        day_output = solution_template.replace("{{DAYNO}}", str(day_no)).replace(
            "{{ascii}}", ascii
        )
        f.writelines(day_output)

    # create the empty input files
    input_filename1 = os.path.join(day_dir, "input.txt")
    input_filename2 = os.path.join(day_dir, "input_simple.txt")
    open(input_filename1, "w")
    open(input_filename2, "w")
