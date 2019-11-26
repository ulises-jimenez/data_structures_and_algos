from typing import List

input_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        columns = len(matrix[0])
        print(rows)
        print(columns)
        rays_holder = [[] for i in range(rows + columns)]
        print(rays_holder)


Solution().findDiagonalOrder(matrix=input_matrix)