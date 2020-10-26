from stack import Stack


def convert_to_base(number: int, base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOP"
    base_stacker = Stack()
    while number > 0:
        remainder = number % base
        number = number // base
        base_stacker.push(remainder)

    base_string = ""
    while not base_stacker.isEmpty():
        base_string = base_string + digits[base_stacker.pop()]

    return base_string


print(convert_to_base(46, 26))
