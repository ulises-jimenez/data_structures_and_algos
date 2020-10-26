import random
from typing import List

list_to_shuffle = [random.randint(0, 100) for x in range(20)]
sorted_list_to_shuffle = sorted(list_to_shuffle)


def bubble_sort(input_list: List):
    for passnum in range(len(input_list) - 1, 0, -1):
        for pointer in range(passnum):
            if input_list[pointer] > input_list[pointer + 1]:
                temp = input_list[pointer]
                input_list[pointer] = input_list[pointer + 1]
                input_list[pointer + 1] = temp


def selection_sort(input_list: List):
    for passnum in range(len(input_list) - 1, 0, -1):
        max_position = 0
        for pointer in range(1, passnum + 1):
            if input_list[pointer] > input_list[max_position]:
                max_position = pointer
        temp = input_list[passnum]
        input_list[passnum] = input_list[max_position]
        input_list[max_position] = temp


selection_sort(list_to_shuffle)
# bubble_sort(list_to_shuffle)
print(list_to_shuffle == sorted_list_to_shuffle)
