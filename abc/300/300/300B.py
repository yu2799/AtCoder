from sys import stdin


def main():
    def check():
        for i in range(h):
            for j in range(w):
                if a[i][j] != b[i][j]:
                    return False
        return True

    input = stdin.readline
    h, w = map(int, input().split())
    a = [list(input()[:-1]) for _ in range(h)]
    b = [list(input()[:-1]) for _ in range(h)]
    for _ in range(h):
        a = a[1:] + [a[0]]
        for _ in range(w):
            for i in range(h):
                a[i] = a[i][1:] + [a[i][0]]
            if check():
                print("Yes")
                return
    print("No")


if __name__ == "__main__":
    main()
