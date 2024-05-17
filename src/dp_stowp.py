from math import sqrt


def calculate_wire_length(horizontal_distance, vertical_distance):
    return sqrt(horizontal_distance ** 2 + vertical_distance ** 2)


def find_max_wire_length(distance, heights):
    num_columns = len(heights)
    if num_columns == 1:
        return 0

    max_top_length = 0
    max_bottom_length = 0

    for idx in range(num_columns - 1):
        bottom_to_bottom = distance
        height_difference = abs(heights[idx] - heights[idx + 1])
        max_max = calculate_wire_length(distance, height_difference)
        min_max = calculate_wire_length(distance, max(heights[idx + 1] - 1, 0))
        max_min = calculate_wire_length(distance, max(heights[idx] - 1, 0))

        next_top_length = max(max_max + max_top_length, min_max + max_bottom_length)
        next_bottom_length = max(max_min + max_top_length, bottom_to_bottom + max_bottom_length)

        max_top_length = next_top_length
        max_bottom_length = next_bottom_length

    return round(max(max_top_length, max_bottom_length), 2)
