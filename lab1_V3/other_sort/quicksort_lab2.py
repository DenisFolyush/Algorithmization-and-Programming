def quicksort(array):
    def partition(left_l, right_l):
        if right_l - left_l < 1:
            return
        pivot = array[left_l]
        left_idx = left_l + 1
        right_idx = right_l
        while True:
            while left_idx <= right_l and array[left_idx] <= pivot:
                left_idx += 1
            while right_idx >= left_l and array[right_idx] > pivot:
                right_idx -= 1
            if left_idx >= right_idx:
                break
            array[left_idx], array[right_idx] = array[right_idx], array[left_idx]
        array[left_l], array[right_idx] = array[right_idx], array[left_l]
        partition(left_l, right_idx - 1)
        partition(right_idx + 1, right_l)

    partition(0, len(array) - 1)
    return array


def sorting(array):
    sorted_nums = quicksort(array[:])
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