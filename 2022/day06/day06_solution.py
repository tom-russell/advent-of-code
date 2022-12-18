# --- day06 ---
#   ______            _                ______                 __    __   
#  /_  __/_  ______  (_)___  ____ _   /_  __/________  __  __/ /_  / /__ 
#   / / / / / / __ \/ / __ \/ __ `/    / / / ___/ __ \/ / / / __ \/ / _ \
#  / / / /_/ / / / / / / / / /_/ /    / / / /  / /_/ / /_/ / /_/ / /  __/
# /_/  \__,_/_/ /_/_/_/ /_/\__, /    /_/ /_/   \____/\__,_/_.___/_/\___/ 
#                         /____/                                         
# 

def load_input(filename):
    lines = []
    with open(filename) as f:
         while x:= f.readline():
            lines.append(x.strip())
    return lines


def has_repeats(marker: str):
    for i in marker:
        if marker.count(i) > 1:
            return True
    return False


def part1(input):
    packet = input[0]
    start_index = 0
    while True:
        if start_index + 4 > len(packet):
            raise RuntimeError()
        marker = packet[start_index:start_index + 4]
        print(marker)

        if not has_repeats(marker):
            break

        start_index += 1

    print(f"marker: {start_index + 4}")


def part2(input):
    packet = input[0]
    start_index = 0
    while True:
        if start_index + 14 > len(packet):
            raise RuntimeError()
        marker = packet[start_index:start_index + 14]
        print(marker)

        if not has_repeats(marker):
            break

        start_index += 1

    print(f"marker: {start_index + 14}")


if __name__ == "__main__":
    dir = '/'.join(__file__.split('/')[:-1])

    # input = load_input(dir + '/input_simple.txt')
    input = load_input(dir + '/input.txt')

    # part1(input)
    part2(input)
