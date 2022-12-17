import os
from pathlib import Path


def get_item_priority(char):
    char_ord = ord(char)
    return char_ord - 38 if char_ord < 97 else char_ord - 96


def solve_part_one(rucksacks):
    res = 0
    for sack in rucksacks:
        sack_len_half = len(sack) // 2
        compartment_a = set(sack[:sack_len_half])
        compartment_b = set(sack[sack_len_half:])
        res += get_item_priority(compartment_a.intersection(compartment_b).pop())
    print(f"Part one (priority sum for mispacked items):\n{res}")


def solve_part_two(rucksacks):
    res = 0
    for i in range(0, len(rucksacks), 3):
        group = [set(sack) for sack in rucksacks[i : i + 3]]
        res += get_item_priority(group[0].intersection(*group[1:]).pop())
    print(f"Part two (badges shared between each set of three):\n{res}")


if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(__file__), "input.txt")
    rucksacks = Path(filepath).read_text().splitlines()
    solve_part_one(rucksacks)
    solve_part_two(rucksacks)
