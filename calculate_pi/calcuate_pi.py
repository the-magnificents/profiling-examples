import random
import sys
import math
import time


def calculate_pi(num_points: int) -> float:
    inside_unit_circle = 0
    pi = 0

    for _ in range(num_points):
        point_x = random.uniform(-1, 1)
        point_y = random.uniform(-1, 1)

        if (math.sqrt(point_x**2 + point_y**2)) < 1.0:
            inside_unit_circle += 1

    pi = (4 * inside_unit_circle) / num_points
    return pi


def main():
    num_points = int(sys.argv[1])
    pi = calculate_pi(num_points)
    print("Pi is ", pi)


if __name__ == "__main__":
    main()
