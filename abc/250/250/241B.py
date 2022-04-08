from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    flag = [True] * n
    for i in b:
        for j in range(len(a)):
            if i == a[j] and flag[j]:
                flag[j] = False
                break
        else:
            print("No")
            break
    else:
        print("Yes")


if __name__ == "__main__":
    main()
