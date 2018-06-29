from functools import reduce

def is_happy_list(numbers: list) -> list:
    return list(map(is_happy,numbers))

def sum_of_squares(number: int) -> int:
    return sum([int(digit)**2 for digit in str(number)])

def is_happy(number: int) -> bool:
    result=number
    while True:
        result = sum_of_squares(result)
        if result == 1:
            return True
        if result < 10:
            return False