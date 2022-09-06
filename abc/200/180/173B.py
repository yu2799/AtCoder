from collections import Counter
from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    s = Counter(input()[:-1] for _ in [0] * n)
    print(f"AC x {s['AC']}")
    print(f"WA x {s['WA']}")
    print(f"TLE x {s['TLE']}")
    print(f"RE x {s['RE']}")


if __name__ == "__main__":
    main()
