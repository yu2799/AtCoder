from sys import stdin


def main():
    input = stdin.readline
    a, b, c = map(int, input().split())
    k = int(input())
    for i in range(k + 1):
        for j in range(k + 1):
            for tmp in range(k + 1):
                if i + j + tmp <= k and a * pow(2, i) < b * pow(
                    2, j
                ) < c * pow(2, tmp):
                    print("Yes")
                    return
    print("No")


if __name__ == "__main__":
    main()
