from typing import List

subarray_example = [2, 1, 5, 1, 3, 2]
k = 3


def find_average_of_subarrays(number_list: List[int], length: int):
    avg_num_list = []
    number_list_len = len(number_list)
    end_num_for_range = number_list_len - length + 1
    for num in range(end_num_for_range):
        relevent_numbers = number_list[num:num + length]
        number_mean = sum(relevent_numbers) / length
        avg_num_list.append(number_mean)
    print(avg_num_list)


def find_average_of_subarrays_optimized(number_list: List[int], length: int):
    avg_num_list = []
    num_list_len = len(number_list)
    end_of_range = num_list_len - length + 1
    for num in range(end_of_range):
        if num == 0:
            relevent_numbers = number_list[num:num + length]
        else:
            relevent_numbers.pop(0)
            relevent_numbers.append(number_list[num + length - 1])
        number_mean = sum(relevent_numbers) / length
        avg_num_list.append(number_mean)
    print(avg_num_list)


def find_largest_sum_array_brute(number_list, length):
    largest_subarray = []
    for num in range(len(number_list) - length + 1):
        current_subarray = number_list[num:num + length]
        current_sum = sum(current_subarray)
        if num == 0:
            largest_subarray_sum = current_sum
            largest_subarray = current_subarray
        else:
            if current_sum > largest_subarray_sum:
                largest_subarray_sum = current_sum
                largest_subarray = current_subarray
    print(largest_subarray)
    print(largest_subarray_sum)


def find_largest_sum_array_optimized(number_list, length):
    largest_subarray = []
    largest_subarray_sum = 0
    window_sum = 0
    for num in range(len(number_list) - length + 1):
        if num == 0:
            for subarray_num in range(num, num + length):
                window_sum += number_list[subarray_num]
        else:
            window_sum -= number_list[num - 1]
            window_sum += number_list[num + length - 1]
        if window_sum > largest_subarray_sum:
            largest_subarray_sum = window_sum
            largest_subarray = number_list[num:num + length]
    print(largest_subarray)
    print(largest_subarray_sum)


def main():
    find_largest_sum_array_brute(number_list=subarray_example, length=k)
    find_largest_sum_array_optimized(number_list=subarray_example, length=k)


if __name__ == '__main__':
    main()
