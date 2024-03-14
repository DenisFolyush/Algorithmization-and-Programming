def insertionsort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
    return array


def sorting(array):
    sorted_nums = insertionsort(array[:])  # Make a copy to not modify the original array
    start = 0
    end = len(array) - 1

    while start < end and array[start] == sorted_nums[start]:
        start += 1

    while end > start and array[end] == sorted_nums[end]:
        end -= 1

    if start >= end:
        return -1, -1

    return start, end


if __name__ == '__main__':
    array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
    # # array = [1, 2, 3, 4, 5]
    # array = [1]
    start, end = sorting(array)
    if start == -1 and end == -1:
        print("list sorted.")
    else:
        print(f"in range [{start}, {end}] needs to be sort.")
