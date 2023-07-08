from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    x = [0] * n
    y = [0] * n
    for i in range(n):
        x[i], y[i] = map(int, input().split())

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            for k in range(n):
                if i == k or j == k:
                    continue
                if (x[i] - x[j]) * (y[k] - y[i]) == (y[i] - y[j]) * (
                    x[k] - x[i]
                ):
                    print("Yes")
                    return
    print("No")


if __name__ == "__main__":
    main()
