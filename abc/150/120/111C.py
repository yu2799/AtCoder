from collections import Counter
from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    v = list(map(int, input().split()))
    even = Counter(v[::2]).most_common(2)
    odd = Counter(v[1::2]).most_common(2)
    if even[0][0] != odd[0][0]:
        print(n - even[0][1] - odd[0][1])
    else:
        if len(even) == 1 or len(odd) == 1:
            print(n // 2)
        else:
            print(n - max(even[0][1] + odd[1][1], odd[0][1] + even[1][1]))


if __name__ == "__main__":
    main()
