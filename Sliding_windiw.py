def sliding_window_sorting(array):
    left, right = 0, len(array) - 1

    while left < len(array) - 1 and array[left] <= array[left + 1]:
        left += 1

    if left == len(array) - 1:
        return -1, -1

    while right > 0 and array[right] >= array[right - 1]:
        right -= 1

    subarray_min = min(array[left:right + 1])
    subarray_max = max(array[left:right + 1])

    while left > 0 and array[left - 1] > subarray_min:
        left -= 1

    while right < len(array) - 1 and array[right + 1] < subarray_max:
        right += 1

    return left, right


def sorting(array):
    start, end = sliding_window_sorting(array[:])
    if start == -1 and end == -1:
        return -1, -1
    else:
        return start, end


array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
# array = [1, 2, 3, 4, 5]
# array = [1]
result = sorting(array)
print(result)
