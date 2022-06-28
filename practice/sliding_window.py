from typing import List

example_array = [2, 3, 4, 1, 5]
k = 2


def calculate_average_of_sub_arrays(array: List,
                                    sub_array_len: int):
    array_of_averages = []
    beginning_of_last_window = len(array) - sub_array_len + 1
    current_array_sum = 0
    for pointer in range(beginning_of_last_window):
        pointer_window_end = pointer + k
        print(pointer, pointer_window_end)
        print(array[pointer:pointer_window_end])
        if pointer == 0:
            for sub_window_pointer in range(pointer, pointer_window_end):
                current_array_sum = current_array_sum + array[sub_window_pointer]
        else:
            current_array_sum = current_array_sum - array[pointer] + array[pointer_window_end]
        current_array_avg = current_array_sum / 5
        array_of_averages.append(current_array_avg)
    print(array_of_averages)


def find_maximum_subarray_sum_on2(array: List,
                                  sub_array_len: int):
    beginning_of_last_window = len(array) - sub_array_len
    subarrays = []
    current_max_subarray_sum = 0
    max_subarray = []
    for pointer in range(beginning_of_last_window + 1):
        current_subarray_sum = 0
        current_subarray = []
        for sub_array_pointer in range(pointer, pointer + sub_array_len):
            current_subarray_sum += array[sub_array_pointer]
            current_subarray.append(array[sub_array_pointer])
        if current_subarray_sum > current_max_subarray_sum:
            current_max_subarray_sum = current_subarray_sum
            max_subarray = current_subarray
        subarrays.append(current_subarray_sum)
    print(f'subarray with max sum: {max_subarray}')
    print(f'max subarray sum: {current_max_subarray_sum}')


def find_maximum_subarray_sum_on(array: List,
                                 sub_array_len: int):
    max_sum = 0
    max_sub_array = []
    current_sum = 0
    current_sub_array = []
    window_start_pointer = 0
    for window_end_pointer in range(len(array)):
        if window_end_pointer < sub_array_len:
            current_sum += array[window_end_pointer]
            current_sub_array.append(array[window_end_pointer])
        else:
            current_sum = current_sum + array[window_end_pointer] - array[window_start_pointer]
            current_sub_array.append(array[window_end_pointer])
            current_sub_array.pop(0)
            if current_sum > max_sum:
                max_sum = current_sum
            else:
                pass
            window_start_pointer += 1
    print(f'max subarray sum: {max_sum}')


if __name__ == '__main__':
    # calculate_average_of_sub_arrays(array=example_array, sub_array_len=k)
    find_maximum_subarray_sum_on2(array=example_array, sub_array_len=k)
    find_maximum_subarray_sum_on(array=example_array, sub_array_len=k)
