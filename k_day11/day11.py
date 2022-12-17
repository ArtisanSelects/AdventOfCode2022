import os
from pathlib import Path
from math import floor, prod

operations = {"+": lambda x, y: x + y, "-": lambda x, y: x - y, "*": lambda x, y: x * y}


class Monkey:
    def __init__(
        self, id, starting_items, operation, test_value, throw_targets, puzzle_part
    ):
        self.id = id
        self.items = starting_items
        self.operation_operand = operation[0]
        self.operation_value_is_old = operation[1] == "old"
        self.operation_value = 0 if self.operation_value_is_old else int(operation[1])
        self.test_value = test_value
        self.throw_targets = throw_targets
        self.items_inspected = 0
        self.part_one = puzzle_part == 1

    def perform_test(self):
        item = self.items.pop()
        self.items_inspected += 1
        item = operations[self.operation_operand](
            item, item if self.operation_value_is_old else self.operation_value
        )
        if self.part_one:
            item = floor(item / 3)
        else:
            item %= self.worry_divisor
        throw_target = 1 if item % self.test_value == 0 else 0
        return (item, self.throw_targets[throw_target])

    def receive_item(self, item):
        self.items.append(item)

    def set_worry_divisor(self, value):
        self.worry_divisor = value


def monkey_parser(monkey_data, puzzle_part):
    res = []
    for i in range(0, len(monkey_data), 7):
        # Monkey 0
        id = int(monkey_data[i].split(" ")[-1].replace(":", ""))
        # Starting items: 79, 98
        starting_items = list(map(int, monkey_data[i + 1][18:].split(", ")))
        # Operation: new = old * 19
        operation_operand, operation_value = monkey_data[i + 2].split(" ")[-2:]
        operation = (operation_operand, operation_value)
        # Test: divisible by 23
        test_value = int(monkey_data[i + 3].split(" ")[-1])
        # If true: throw to monkey 2
        true_target = int(monkey_data[i + 4].split(" ")[-1])
        # If false: throw to monkey 3
        false_target = int(monkey_data[i + 5].split(" ")[-1])
        throw_targets = (false_target, true_target)
        res.append(
            Monkey(
                id, starting_items, operation, test_value, throw_targets, puzzle_part
            )
        )
    return res


def set_worry_divisor(monkeys):
    worry_divisor = prod(monkey.test_value for monkey in monkeys)
    for monkey in monkeys:
        monkey.set_worry_divisor(worry_divisor)


def solve_puzzle(monkey_data, puzzle_part):
    monkeys = monkey_parser(monkey_data, puzzle_part)
    rounds = 20
    if puzzle_part == 2:
        rounds = 10000
        set_worry_divisor(monkeys)
    for _ in range(rounds):
        for monkey in monkeys:
            for _ in range(len(monkey.items)):
                item_value, target_monkey = monkey.perform_test()
                monkeys[target_monkey].receive_item(item_value)
    res = sorted([monkey.items_inspected for monkey in monkeys], reverse=True)
    return res[0] * res[1]


if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(__file__), "input.txt")
    monkey_data = Path(filepath).read_text().splitlines()
    part_one = solve_puzzle(monkey_data, 1)
    print(f"Part one (product of top two inspectors):\n{part_one}")
    part_two = solve_puzzle(monkey_data, 2)
    print(f"Part two (custom worry divisor):\n{part_two}")
