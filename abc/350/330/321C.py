from itertools import product
from sys import stdin


def main():
    input = stdin.readline
    k = int(input())
    res = []
    tmp = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    for bits in product([0, 1], repeat=10):
        a = [str(x) for bit, x in zip(bits, tmp) if bit == 1]
        if not a:
            continue
        res.append(int("".join(a)))
    res.sort()
    print(res[k])


if __name__ == "__main__":
    main()
