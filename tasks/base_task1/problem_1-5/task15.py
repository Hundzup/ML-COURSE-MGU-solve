from typing import List


def hello(name: str = None) -> str:
    if name == None or name == "":
        return "Hello!"
    return "Hello, " + name + "!"


def int_to_roman(num: int) -> str:
    result = ""
    if num // 1000 != 0:
        result += "M" * (num // 1000)
        num -= 1000 * (num // 1000)
    if num - 900 >= 0:
        result += "CM"
        num -= 900
    if num // 500 != 0:
        result += "D"
        num -= 500
    if num - 400 >= 0:
        result += "CD"
        num -= 400
    if num // 100 != 0:
        result += "C" * (num // 100)
        num -= 100 * (num // 100)
    if num - 90 >= 0:
        result += "XC"
        num -= 90
    if num // 50 != 0:
        result += "L"
        num -= 50
    if num - 40 >= 0:
        result += "XL"
        num -= 40
    if num // 10 != 0:
        result += "X" * (num // 10)
        num -= 10 * (num // 10)
    if num - 9 >= 0:
        result += "IX"
        num -= 9
    if num // 5 != 0:
        result += "V"
        num -= 5
    if num - 4 >= 0:
        result += "IV"
        num -= 4
    if num // 1 != 0:
        result += "I" * (num // 1)
    return result


def longest_common_prefix(strs_input: List[str]) -> str:
    if not strs_input:
        return ""
    strs = [s.lstrip() for s in strs_input]
    shortest = min(strs, key=len)

    for i, ch in enumerate(shortest):
        for s in strs:
            if s[i] != ch:
                return shortest[:i]

    return shortest


def primes() -> int:
    yield


class BankCard:
    def __init__(self, total_sum: int, balance_limit: int = -1):
        self.total_sum = total_sum
        self.balance_limit = balance_limit

    def __call__(self, sum_spend):
        if sum_spend <= self.total_sum:
            self.total_sum -= sum_spend
            print(f"You spend {sum_spend} dollars.")
        else:
            raise ValueError("Not enough money to spend sum_spent dollars.")

    def __repr__(self):
        return "To learn the balance call balance."

    @property
    def balance(self):
        if self.balance_limit == 0:
            raise ValueError("Balance check limits exceeded.")
        else:
            self.balance_limit -= 1
            return self.total_sum

    def put(self, sum_put):
        self.total_sum += sum_put
        print(f"You put {sum_put} dollars.")

    def __add__(self, x):
        self.total_sum += x.total_sum
        if self.balance_limit < x.balance_limit:
            self.balance_limit = x.balance_limit
        return BankCard(self.total_sum, self.balance_limit)
