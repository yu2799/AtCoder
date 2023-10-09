from itertools import product
from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    if n % 2:
        return
    buf = ["(", ")"]
    for i in product(buf, repeat=n):
        cnt = 0
        for j in i:
            if j == "(":
                cnt += 1
            else:
                if cnt == 0:
                    break
                cnt -= 1
        else:
            if cnt == 0:
                print("".join(i))


if __name__ == "__main__":
    main()
