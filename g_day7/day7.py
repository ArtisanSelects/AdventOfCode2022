import os
from pathlib import Path
from collections import defaultdict


def solve_puzzle(commands):
    dirs = defaultdict(int)
    cwd = []
    for command in commands:
        command = command.split(' ')
        if command[1] == 'ls':
            continue
        if command[0] == '$':
            value = command[2]
            if value == '..':
                cwd.pop()
            else:
                cwd.append(value)
        elif command[0] != 'dir':
            file_size = int(command[0])
            cur_dir = ''
            for dir in cwd:
                cur_dir = f'{cur_dir}/{dir}'
                dirs[cur_dir] += file_size

    part_one_max_size = 100000
    part_one = sum(v for v in dirs.values() if v <= part_one_max_size)
    print(f'Part one (All directories <= 100,000):\n{part_one}')

    part_two_max_size = 30000000 - (70000000 - max(dirs.values()))
    part_two = min(v for v in dirs.values() if v >= part_two_max_size)
    print(f'Part two (smallest directory to free up enough space):\n{part_two}')
    

if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(__file__), 'input.txt')
    commands = Path(filepath).read_text().splitlines()
    solve_puzzle(commands)