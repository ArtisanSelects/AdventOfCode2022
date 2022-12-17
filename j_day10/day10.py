import os
from pathlib import Path


def solve_part_one(instructions):
    register = 1
    cycle = 0
    res = 0
    target_cycles = set([20, 60, 100, 140, 180, 220])
    for ins in instructions:
        if ins[:4] == "noop":
            cycle += 1
            if cycle in target_cycles:
                res += register * cycle
        else:
            cur_cycle = set([cycle + 1, cycle + 2]).intersection(target_cycles)
            if cur_cycle:
                res += register * cur_cycle.pop()
            cycle += 2
            _, val = ins.split(" ")
            register += int(val)
    print(f"Part one (sum during target cycles):\n{res}")


def solve_part_two(instructions):
    register = 1
    cycle = -1
    horiz = 40
    res = [[] for _ in range(6)]
    for ins in instructions:
        is_noop = ins[:4] == "noop"
        for _ in range(1 if is_noop else 2):
            cycle += 1
            active_pixels = (register - 1, register, register + 1)
            res[cycle // horiz].append("#" if cycle % horiz in active_pixels else ".")
        if not is_noop:
            _, value = ins.split(" ")
            register += int(value)

    for row in res:
        print(" ".join(row))


if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(__file__), "input.txt")
    instructions = Path(filepath).read_text().splitlines()
    solve_part_one(instructions)
    solve_part_two(instructions)
