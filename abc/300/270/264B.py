from sys import stdin


def main():
    input = stdin.readline
    r, c = map(int, input().split())
    grid = [
        "###############",
        "#.............#",
        "#.###########.#",
        "#.#.........#.#",
        "#.#.#######.#.#",
        "#.#.#.....#.#.#",
        "#.#.#.###.#.#.#",
        "#.#.#.#.#.#.#.#",
        "#.#.#.###.#.#.#",
        "#.#.#.....#.#.#",
        "#.#.#######.#.#",
        "#.#.........#.#",
        "#.###########.#",
        "#.............#",
        "###############",
    ]
    print("black" if grid[c - 1][r - 1] == "#" else "white")


if __name__ == "__main__":
    main()
