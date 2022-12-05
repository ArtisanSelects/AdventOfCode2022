import os
from pathlib import Path


def solve_puzzle(groups):
    def group_to_set(group):
        start, end = map(int, group.split('-'))
        return set(range(start, end+1))

    res_part_one = 0
    res_part_two = 0
    for group in groups:
        a, b = (group_to_set(i) for i in group.split(','))
        if not a.difference(b) or not b.difference(a):
            res_part_one += 1
        if a.intersection(b):
            res_part_two += 1
    print(f"Part one (groups that totally overlap):\n{res_part_one}")
    print(f"Part two (groups that have any overlap):\n{res_part_two}")


if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(__file__), 'input.txt')
    groups = Path(filepath).read_text().splitlines()
    solve_puzzle(groups)