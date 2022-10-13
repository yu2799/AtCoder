from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    a = list(map(int, input().split()))
    odd = []
    even = []
    for i in a:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    odd_l = len(odd)
    even_l = len(even)
    odd.sort()
    even.sort()
    if odd_l < 2 and even_l < 2:
        print(-1)
    elif odd_l < 2:
        print(sum(even[-2:]))
    elif even_l < 2:
        print(sum(odd[-2:]))
    else:
        print(
            sum(even[-2:]) if sum(odd[-2:]) < sum(even[-2:]) else sum(odd[-2:])
        )


if __name__ == "__main__":
    main()
