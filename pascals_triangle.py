from typing import List

row_number = 5


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        top_level_list = []
        for num in range(numRows):
            top_level_list.append([])

        for num in range(numRows):
            if num == 0:
                top_level_list[num] = [1]
            else:
                for cell in range(num + 1):
                    if cell == 0:
                        top_level_list[num].insert(cell, top_level_list[num - 1][0])
                    elif cell == num:
                        top_level_list[num].insert(cell, top_level_list[num - 1][-1])
                    else:
                        top_level_list[num].insert(cell,
                                                   top_level_list[num - 1][cell - 1] + top_level_list[num - 1][cell])

        return top_level_list


print(Solution().generate(row_number))
