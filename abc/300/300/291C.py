from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    s = input()[:-1]
    visited = set([(0, 0)])
    cur_x = 0
    cur_y = 0
    for i in s:
        if i == "L":
            cur_x -= 1
        if i == "R":
            cur_x += 1
        if i == "U":
            cur_y += 1
        if i == "D":
            cur_y -= 1
        if (cur_x, cur_y) in visited:
            print("Yes")
            return
        visited.add((cur_x, cur_y))
    print("No")


if __name__ == "__main__":
    main()
