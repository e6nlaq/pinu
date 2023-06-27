from random import randint
import sys
from pinu.lib.is_num import is_num


def run() -> None:
    args: list[str] = sys.argv

    if len(args) != 2:
        print("Argument length must be 2")
        return 1
    elif is_num(args[0]) and is_num(args[1]):
        a: int = int(args[0])
        b: int = int(args[1])

        print(prand(a, b))
        return 0
    else:
        print("Argument must be a number")
        return 1


def prand(a: int, b: int) -> int:
    if a == b:
        return a
    elif a > b:
        a, b = b, a

    return randint(a, b)
