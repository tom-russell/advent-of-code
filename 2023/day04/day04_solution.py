# --- day04 ---
#    _____                 __       __                        __     ___
#   / ___/______________ _/ /______/ /_  _________ __________/ /____/  /
#   \__ \/ ___/ ___/ __ `/ __/ ___/ __ \/ ___/ __ `/ ___/ __  / ___// /
#  ___/ / /__/ /  / /_/ / /_/ /__/ / / / /__/ /_/ / /  / /_/ (__  )/ /
# /____/\___/_/   \__,_/\__/\___/_/ /_/\___/\__,_/_/   \__,_/____// /
#                                                               /__/
#


def load_input(filename):
    lines = []
    with open(filename) as f:
        while x := f.readline():
            lines.append(x.strip())
    return lines


SCORE_MAP = {
    0: 0,
    1: 1,
    2: 2,
    3: 4,
    4: 8,
    5: 16,
    6: 32,
    7: 64,
    8: 128,
    9: 256,
    10: 512,
}


class ScratchCard:
    def __init__(self, input: str):
        self.card_no = int(input.split(":")[0][5:])
        self.index = self.card_no - 1
        all_numbers = input.split(": ")[1].split(" | ")
        self.winning_numbers = {int(x) for x in all_numbers[0].split()}
        self.my_numbers = {int(x) for x in all_numbers[1].split()}

    def win_count(self) -> int:
        return len(self.my_numbers.intersection(self.winning_numbers))

    def score(self) -> int:
        return SCORE_MAP[self.win_count()]


def part1(input):
    sum = 0
    for line in input:
        card = ScratchCard(line)
        sum += card.score()
    print(sum)


def part2(input):
    card_counts = {index: 1 for index, _ in enumerate(input)}

    for index, line in enumerate(input):
        card = ScratchCard(line)
        for win in range(card.win_count()):
            card_counts[index + win + 1] += card_counts[index]

    print(f"{card_counts}")
    print(sum(card_counts.values()))


if __name__ == "__main__":
    dir = "/".join(__file__.split("/")[:-1])
    # input = load_input(dir + "/input_simple.txt")
    input = load_input(dir + '/input.txt')

    # part1(input)
    part2(input)
