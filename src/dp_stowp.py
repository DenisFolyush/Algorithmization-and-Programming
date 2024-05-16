import math


# обчислює довжину дроту між двома опорами
def calculate_distance(width, height1, height2):
    return math.sqrt(width ** 2 + (height2 - height1) ** 2)


def max_wire_length(width, heights):
    num_heights = len(heights)

    # масив який зберігає максимальну довжину дроту до опори i
    dp = [[0] * (h + 1) for h in heights]

    # всі опори 0 мають нульову довжину
    for h in range(1, heights[0] + 1):
        dp[0][h] = 0

    for i in range(1, num_heights):
        for h2 in range(1, heights[i] + 1):
            dp[i][h2] = max(
                dp[i - 1][h1] + calculate_distance(width, h1, h2)
                for h1 in range(1, heights[i - 1] + 1)
            )

    max_length = max(dp[-1])

    return round(max_length, 2)
