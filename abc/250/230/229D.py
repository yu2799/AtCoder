from sys import stdin
from collections import deque


def main():
    input = stdin.readline
    s = input()[:-1]
    k = int(input())
    q = deque()
    cnt = {"X": 0, ".": 0}
    res = 0
    for i in s:
        q.append(i)
        cnt[i] += 1
        while q and k < cnt["."]:
            rm = q.popleft()
            cnt[rm] -= 1
        if res < cnt["X"] + cnt["."]:
            res = cnt["X"] + cnt["."]
    print(res)


if __name__ == "__main__":
    main()
