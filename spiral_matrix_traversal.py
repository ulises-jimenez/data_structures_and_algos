from typing import List

# input_matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]


input_matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]


# input_matrix = [
#     [1, 2]
# ]


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == []:
            return []
        left = 0
        top = 0
        right = len(matrix[0])
        bottom = len(matrix)
        ctrl = 0
        answer_l = []
        while left < right and top < bottom:
            if ctrl == 0:
                current_row = matrix[top]
                for column in range(left, right):
                    answer_l.append(current_row[column])
                top += 1
                ctrl = 1

            elif ctrl == 1:
                current_column = right - 1
                for row in range(top, bottom):
                    answer_l.append(matrix[row][current_column])
                right -= 1
                ctrl = 2

            elif ctrl == 2:
                current_row = matrix[bottom - 1]
                for column in range(right - 1, left - 1, -1):
                    answer_l.append(current_row[column])
                bottom -= 1
                ctrl = 3

            elif ctrl == 3:
                current_column = left
                for row in range(bottom - 1, top - 1, -1):
                    answer_l.append(matrix[row][current_column])
                left += 1
                ctrl = 0
            else:
                raise AssertionError('something went wrong')

        return answer_l


answer_l = Solution().spiralOrder(input_matrix)
print(answer_l)
