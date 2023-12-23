from sys import stdin


def main():
    input = stdin.readline
    a = [list(map(int, input().split())) for _ in range(9)]
    for i in range(9):
        tmp = set()
        for j in range(9):
            tmp.add(a[i][j])
        if len(tmp) != 9:
            print("No")
            return
    for i in range(9):
        tmp = set()
        for j in range(9):
            tmp.add(a[j][i])
        if len(tmp) != 9:
            print("No")
            return

    for i in range(3):
        for j in range(3):
            tmp = set()
            for k in range(3):
                for h in range(3):
                    tmp.add(a[i * 3 + k][j * 3 + h])
            if len(tmp) != 9:
                print("No")
                return
    print("Yes")


if __name__ == "__main__":
    main()
