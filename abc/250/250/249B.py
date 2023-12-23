from collections import defaultdict
from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    upper = False
    lower = False
    d = defaultdict(int)
    for i in s:
        d[i] += 1
        if "A" <= i <= "Z":
            upper = True
        elif "a" <= i <= "z":
            lower = True
    print("Yes" if upper and lower and len(d.keys()) == len(s) else "No")


if __name__ == "__main__":
    main()
