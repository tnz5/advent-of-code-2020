# Day 3 Toboggan Trajectory

MOVES = [[1,1], [3,1], [5,1], [7,1], [1,2]]

def parse_input():
    with open("input.txt", "r") as f:
        input = f.readlines()
        forest = [x.strip() for x in input]
    return forest


def count_trees(forest, right, down):
    x = 0
    y = 0
    num_trees = 0
    while y <= len(forest) - 1:
        curr_loc = forest[y][x]
        if curr_loc == '#':
            num_trees += 1
        x += right
        y += down
    return num_trees


def main():
    input = parse_input()
    # expand width of forest
    forest = [i*len(input) for i in input]

    # Part 1 Total Trees
    num_trees = count_trees(forest, 3, 1)
    print(num_trees)

    # Part 2 Total Trees
    results = [count_trees(forest, c[0], c[1]) for c in MOVES]
    final_product = 1
    for r in results:
        final_product *= r
    print(final_product)


if __name__ == '__main__':
    main()
