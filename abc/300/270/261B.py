from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = [list(input()[:-1]) for _ in [0] * n]
    d = {
        "W": "L",
        "L": "W",
        "D": "D",
    }
    for i in range(n):
        for j in range(i + 1, n):
            if d[a[i][j]] != a[j][i]:
                print("incorrect")
                return
    print("correct")


if __name__ == "__main__":
    main()
