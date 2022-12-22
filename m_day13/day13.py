import os
from pathlib import Path
from functools import cmp_to_key
from ast import literal_eval


def parse_signals(input_text, pair_signals):
    res = []
    i = 0
    while i < len(input_text):
        signal_a = literal_eval(input_text[i])
        signal_b = literal_eval(input_text[i + 1])
        if pair_signals:
            res.append([signal_a, signal_b])
        else:
            res.append(signal_a)
            res.append(signal_b)
        i += 3
    return res


def check_valid_lists(list_a, list_b):
    list_a = list_a[::-1]
    list_b = list_b[::-1]
    while list_a and list_b:
        a = list_a.pop()
        b = list_b.pop()
        if a == b:
            continue
        a_int = isinstance(a, int)
        b_int = isinstance(b, int)
        if a_int and b_int:
            return a < b
        if a_int:
            a = [a]
        if b_int:
            b = [b]
        is_valid = check_valid_lists(a, b)
        if is_valid is not None:
            return is_valid
    if list_a == list_b:
        return None
    return len(list_a) <= len(list_b)


def compare_signals(a, b):
    res = check_valid_lists(a, b)
    if res is None:
        return 0
    return 1 if res else -1


def solve_part_one(signals):
    signals = parse_signals(signals, True)
    res = 0
    for i, pair in enumerate(signals):
        if check_valid_lists(*pair):
            res += i + 1
    return res


def solve_part_two(signals):
    signals = parse_signals(signals, False)
    divider_a = [[2]]
    divider_b = [[6]]
    signals += [divider_a, divider_b]
    signals.sort(key=cmp_to_key(compare_signals), reverse=True)
    divider_a_index = signals.index(divider_a) + 1
    divider_b_index = signals.index(divider_b) + 1
    return divider_a_index * divider_b_index


if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(__file__), "input.txt")
    signals = Path(filepath).read_text().splitlines()
    part_one = solve_part_one(signals)
    print(f"Part one (sum of indicies for valid pairs):\n{part_one}")
    part_two = solve_part_two(signals)
    print(f"Part two (decoder key from dividers)\n{part_two}")
