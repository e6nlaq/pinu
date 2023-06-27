#!/bin/env python3

from random import randint
import sys
import argparse


def prand_run() -> None:
    if len(sys.argv) != 1:
        parser = argparse.ArgumentParser(description="Returns a random number")

        parser.add_argument("arg1", type=int, help="Random minimum")
        parser.add_argument("arg2", type=int, help="Random maximum")

        args = parser.parse_args()

        print(prand(args.arg1, args.arg2))
    else:
        try:
            a, b = map(int, input().split(" "))
            print(prand(a, b))
        except ValueError:
            print("Error: Invalid argument")
            exit(1)

    exit(0)


def prand(a: int, b: int) -> int:
    if a == b:
        return a
    elif a > b:
        a, b = b, a

    return randint(a, b)


if __name__ == "__main__":
    prand_run()
