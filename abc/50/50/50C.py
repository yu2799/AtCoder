from collections import Counter
from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    MOD = 10**9 + 7
    tmp = n % 2
    res = 1
    for key, value in Counter(a).items():
        if key % 2 == tmp or value >= 3:
            print(0)
            return
        if value == 1:
            if key != (n - 1) % 2:
                print(0)
                return
        else:
            res = res * 2 % MOD
    print(res)


if __name__ == "__main__":
    main()
