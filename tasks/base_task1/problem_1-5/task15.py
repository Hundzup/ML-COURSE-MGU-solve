from typing import List


def hello(name: str = None) -> str:
    if name == None or name == "":
        return "Hello!"
    return "Hello, " + name + "!"


def int_to_roman(num: int) -> str:
    pass


def longest_common_prefix(strs_input: List[str]) -> str:
    pass


def primes() -> int:
    yield


class BankCard:
    def __init__(self, total_sum: int, balance_limit: int):
        pass
