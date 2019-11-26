from typing import List

example = [1, 7, 3, 9, 9, 9]


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last_digit = digits[-1]
        first_digit = digits[0]
        if last_digit != 9:
            last_digit_plus_one = last_digit + 1
            digits.pop()
            digits.append(last_digit_plus_one)
            return digits
        else:
            reversed_index = list(range(len(digits)))[::-1]
            number = 0
            for pointer in range(len(digits)):
                adder = digits[pointer] * (10**reversed_index[pointer])
                number += adder
            number += 1
            return [int(str_digit) for str_digit in str(number)]


print(example)
print(Solution().plusOne(example))
