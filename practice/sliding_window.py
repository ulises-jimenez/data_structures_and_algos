from typing import List

subarray_example = [2, 3, 4, 1, 5]
k = 2


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


def main():
    print('main')


if __name__ == '__main__':
    main()
