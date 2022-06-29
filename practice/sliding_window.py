import math
from typing import List

subarray_example = [2, 1, 5, 2, 3, 2]
s = 7


def find_max_subarray_sum_brute(subarray: List[int], subarray_len: int):
    current_max_sum = 0
    current_max_entries = []
    start_pointer = 0
    end_pointer = subarray_len - 1
    beginning_pointer_last_subarray = len(subarray) - subarray_len + 1
    print(subarray)
    for entry in range(start_pointer, beginning_pointer_last_subarray):
        current_sum = 0
        current_end_pointer = entry + subarray_len
        current_entries = subarray[entry:current_end_pointer]
        print(f'current entries: {current_entries}')
        for sum_component in current_entries:
            current_sum += sum_component
        if current_sum > current_max_sum:
            current_max_sum = current_sum
            current_max_entries = current_entries

    print(current_max_sum, current_max_entries)


def find_max_subarray_optimized(subarray: List[int], subarray_len: int):
    starting_pointer = 0
    current_max_sum = 0
    current_max_sequence = []
    last_subarray_pointer_start = len(subarray) - subarray_len + 1
    print(subarray)
    current_sum = 0
    for pointer in range(starting_pointer, last_subarray_pointer_start):
        current_entries = subarray[pointer:pointer + subarray_len]
        print(f'current entries {current_entries}')
        if pointer > 0:
            current_sum -= subarray[pointer - 1]
            current_sum += subarray[pointer + 1]
        else:
            for sum_entry in current_entries:
                current_sum += sum_entry
        if current_sum > current_max_sum:
            current_max_sum = current_sum
            current_max_sequence = current_entries
    print(current_max_sum, current_max_sequence)


def find_shortest_subarray_larger_than_l(input_array: List[int], min_sum: int):
    print(input_array)
    correct_sum = math.inf
    correct_subarray = []
    starting_pointer = 0
    current_sum = 0
    for end_pointer in range(len(input_array)):
        current_subarray = input_array[starting_pointer: end_pointer + 1]
        current_sum += input_array[end_pointer]
        while current_sum >= min_sum:
            if correct_sum == math.inf:
                correct_sum = current_sum
                correct_subarray = current_subarray
            elif len(current_subarray) < len(correct_subarray):
                correct_sum = current_sum
                correct_subarray = current_subarray
            else:
                pass
            starting_pointer += 1
            current_subarray = input_array[starting_pointer: end_pointer + 1]
            current_sum -= input_array[starting_pointer - 1]
    if correct_sum == math.inf:
        print([], 0)
    else:
        print(correct_subarray, correct_sum)


def main():
    find_shortest_subarray_larger_than_l(input_array=subarray_example, min_sum=s)


if __name__ == '__main__':
    main()
