from typing import List


def sequential_search(search_list: List, entry_to_look_for):
    for pointer, entry in enumerate(search_list):
        if entry_to_look_for == entry:
            return True, pointer
    return False, -1


def binary_search(search_list: List[int], search_item: int):
    start = 0
    end = len(search_list) - 1
    found = False
    while start <= end and not found:
        midpoint = (start + end) // 2
        if search_list[midpoint] == search_item:
            found = True
        else:
            if search_list[midpoint] < search_item:
                start = midpoint + 1
            else:
                end = midpoint - 1
    return found


# testlist = [1, 2, 32, 8, 17, 19, 42, 13, l0]
# print(sequential_search(testlist, 3))
# print(sequential_search(testlist, 13))

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
for case in testlist:
    print(binary_search(testlist, case), case)
    print(binary_search(testlist, case + 1), case + 1)


