a = "1"
b = "111"


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_len = len(a)
        b_len = len(b)

        while a_len < b_len:
            a = '0' + a
            a_len = len(a)
        while b_len < a_len:
            b = '0' + b
            b_len = len(b)
        new_str = []
        carry_over = '0'
        for pointer in range(a_len - 1, -1, -1):
            a_digit = a[pointer]
            b_digit = b[pointer]
            if a_digit == '1' and b_digit == '1' and carry_over == '0':
                new_str.insert(0, '0')
                carry_over = '1'
            elif a_digit == '1' and b_digit == '0' and carry_over == '0':
                new_str.insert(0, '1')
                carry_over = '0'
            elif a_digit == '0' and b_digit == '1' and carry_over == '0':
                new_str.insert(0, '1')
                carry_over = '0'
            elif a_digit == '0' and b_digit == '0' and carry_over == '0':
                new_str.insert(0, '0')
                carry_over = '0'
            elif a_digit == '1' and b_digit == '1' and carry_over == '1':
                new_str.insert(0, '1')
                carry_over = '1'
            elif a_digit == '1' and b_digit == '0' and carry_over == '1':
                new_str.insert(0, '0')
                carry_over = '1'
            elif a_digit == '0' and b_digit == '1' and carry_over == '1':
                new_str.insert(0, '0')
                carry_over = '1'
            elif a_digit == '0' and b_digit == '0' and carry_over == '1':
                new_str.insert(0, '1')
                carry_over = '0'
            else:
                raise AssertionError('something went wrong')

            if carry_over == '1' and pointer == 0:
                new_str.insert(0, '1')

        return ''.join(new_str)

print(Solution().addBinary(a, b))
