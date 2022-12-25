from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    left = [0] * n
    right = [0] * n
    for i in range(n):
        t, left[i], right[i] = map(int, input().split())
        if t == 2 or t == 4:
            right[i] -= 0.5
        if t == 3 or t == 4:
            left[i] += 0.5
    res = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if max(left[i], left[j]) <= min(right[i], right[j]):
                res += 1
    print(res)


if __name__ == "__main__":
    main()
