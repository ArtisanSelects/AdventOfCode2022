import os
from pathlib import Path


def solve_puzzle(calories):
    res_part_one = 0
    res_part_two = [0, 0, 0]
    current_total = 0
    for dish in calories:
        if not dish:
            res_part_one = max(res_part_one, current_total)
            if current_total > res_part_two[-1]:
                res_part_two.append(current_total)
                res_part_two = sorted(res_part_two, reverse=True)[:3]
            current_total = 0
            continue
        current_total += int(dish)

    print(f"Part one (the elf with the most calories):\n{res_part_one}")
    print(f"Part two (sum of the top three calorie-heavy elves):\n{sum(res_part_two)}")


if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(__file__), "input.txt")
    calories = Path(filepath).read_text().splitlines()
    solve_puzzle(calories)
