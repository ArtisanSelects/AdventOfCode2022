import os
from pathlib import Path


class Sensor:
    def __init__(self, input_string):
        # Sensor at x=20, y=1: closest beacon is at x=15, y=3
        sensor, beacon = input_string.split(": closest beacon is at ")
        self.sensor_x, self.sensor_y = self._parse_coord_string(sensor[10:])
        self.beacon_x, self.beacon_y = self._parse_coord_string(beacon)
        self.max_range = self._get_dist(
            (self.beacon_x, self.beacon_y), (self.sensor_x, self.sensor_y)
        )

    @staticmethod
    def _parse_coord_string(coord_string):
        x, y = coord_string.split(", ")
        return (int(x[2:]), int(y[2:]))

    @staticmethod
    def _get_dist(a, b):
        return sum(abs(i - j) for i, j in zip(a, b))

    def normalize(self, x, y):
        self.sensor_x -= x
        self.beacon_x -= x
        self.sensor_y -= y
        self.beacon_y -= y

    def get_row_coords_in_range(self, row_y):
        in_range, x_start, x_end = self.get_x_range_for_row(row_y)
        if not in_range:
            return set()
        res = set(range(x_start, x_end + 1))
        if self.beacon_y == row_y and self.beacon_x in res:
            res.remove(self.beacon_x)
        return res

    def get_x_range_for_row(self, row_y):
        max_range = self.max_range - abs(self.sensor_y - row_y)
        if max_range <= 0:
            return (False, 0, 0)
        x_start = self.sensor_x - max_range
        x_end = self.sensor_x + max_range
        return (True, x_start, x_end)


def generate_sensors(beacon_sensor_list, target_row):
    sensors = [Sensor(i) for i in beacon_sensor_list]
    min_x = min(sensor.sensor_x for sensor in sensors)
    min_y = min(sensor.sensor_y for sensor in sensors)
    for sensor in sensors:
        sensor.normalize(min_x, min_y)
    target_row -= min_y
    return (sensors, target_row, min_x, min_y)


def solve_part_one(beacon_sensor_list, target_row):
    sensors, target_row, *_ = generate_sensors(beacon_sensor_list, target_row)
    res = set()
    for sensor in sensors:
        res.update(sensor.get_row_coords_in_range(target_row))
    return len(res)


def solve_part_two(beacon_sensor_list, max_y):
    sensors, max_y, min_x, min_y = generate_sensors(beacon_sensor_list, max_y)
    max_x = max(sensor.sensor_x for sensor in sensors)
    for y in range(0, max_y):
        intervals_initial = [sensor.get_x_range_for_row(y) for sensor in sensors]
        intervals = []
        for interval in intervals_initial:
            in_range, x_start, x_end = interval
            if in_range:
                intervals.append((max(0, x_start), min(max_x, x_end)))
        intervals.sort()
        last_max = intervals[0][1]
        for interval in intervals[1:]:
            start, end = interval
            if end <= last_max:
                continue
            if start > last_max:
                return (start - 1 + min_x) * (max_y + min_y) + (y + min_y)
            last_max = end


if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(__file__), "input.txt")
    beacon_sensor_list = Path(filepath).read_text().splitlines()
    part_one = solve_part_one(beacon_sensor_list, 2000000)
    print(f"Part one (where beacon can't be):\n{part_one}")
    part_two = solve_part_two(beacon_sensor_list, 4000000)
    print(f"Part two (tuning frequency of beacon):\n{part_two}")
