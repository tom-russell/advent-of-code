# --- day01 ---
#   ______          __               __         __ ___  __
#  /_  __/_______  / /_  __  _______/ /_  ___  / //__ \/ /
#   / / / ___/ _ \/ __ \/ / / / ___/ __ \/ _ \/ __// _/ /
#  / / / /  /  __/ /_/ / /_/ / /__/ / / /  __/ /_ /_//_/
# /_/ /_/   \___/_.___/\__,_/\___/_/ /_/\___/\__/(_)(_)
#
#


NUMBER_MAP = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}


def load_input(filename):
    lines = []
    with open(filename) as f:
        while x := f.readline():
            lines.append(x.strip())
    return lines


def part1(input):
    sum = 0
    for line in input:
        parsed_input = [char for char in list(line) if char.isnumeric()]
        sum += int(parsed_input[0] + parsed_input[-1])
    print(sum)


def get_matches(line: str, key: str):
    if key not in line:
        return []

    return [line.find(key), line.rfind(key)]


def part2(input):
    """
    Build a data structure like this, to represent the index of any digit matches.
    For the example `two1nine`:
    {
        0: "2",
        3: "1",
        4: "9",
    }
    """
    sum = 0

    for line in input:
        index_map = {}
        for key, value in NUMBER_MAP.items():
            matches = get_matches(line, key)
            for match in matches:
                index_map[match] = value

        sum += int(index_map[min(index_map.keys())] + index_map[max(index_map.keys())])
    print(sum)


def part_2_alternate(input):
    sum = 0
    for line in input:
        char_list = list(line)
        parsed = []
        for index in range(len(char_list)):
            for digit, value in NUMBER_MAP.items():
                if "".join(char_list[int(index):]).startswith(digit):
                    parsed.append(value)
        sum += int(parsed[0] + parsed[-1])
    print(sum)


if __name__ == "__main__":
    dir = "/".join(__file__.split("/")[:-1])
    # input = load_input(dir + "/input_simple_2.txt")
    input = load_input(dir + "/input.txt")

    # part1(input)
    # part2(input)
    part_2_alternate(input)
