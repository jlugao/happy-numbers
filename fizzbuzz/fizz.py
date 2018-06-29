
from functools import partial, wraps
from typing import Any


def compose(*funcs):
    def inner(arg):
        state = arg
        for func in funcs:
            state = func(state)
        return state
    return inner

def is_int(func):

    @wraps(func)
    def inner(val):
        return func(val) if isinstance(val, int) else val
    return inner

def is_divisible_by_n(divisor: int, number: int) -> int:
    return number % divisor == 0

is_divisible_by_3 = partial(is_divisible_by_n, 3)
is_divisible_by_5 = partial(is_divisible_by_n, 5)

@is_int
def fizz(number: int) -> Any:
    return 'Fizz' if is_divisible_by_3(number) else number

@is_int
def buzz(number: int) -> Any:
    return 'Buzz' if is_divisible_by_5(number) else number

@is_int
def _fizzbuzz(number: int) -> Any:
    return 'FizzBuzz' if is_divisible_by_3(number) and is_divisible_by_5(number) else number

@is_int
def justnumber(number: int) -> str:
    return str(number)

fizzbuzz = compose(_fizzbuzz, buzz, fizz, justnumber)
fizzbuzzlist = compose(partial(map,fizzbuzz),list)

# def fizzbuzz(number: int) -> str:
#     if is_divisible_by_3(number) and is_divisible_by_5(number):
#         return 'FizzBuzz'
#     if is_divisible_by_5(number):
#         return 'Buzz'
#     if is_divisible_by_3(number):
#         return 'Fizz'
#     return str(number)