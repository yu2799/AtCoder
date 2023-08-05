from itertools import permutations
from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    s = [input()[:-1] for _ in range(n)]
    for item in permutations(s):
        for i in range(n - 1):
            cnt = 0
            for j in range(m):
                if item[i][j] != item[i + 1][j]:
                    cnt += 1
                if cnt == 2:
                    break
            else:
                continue
            break
        else:
            print("Yes")
            return
    print("No")


if __name__ == "__main__":
    main()
