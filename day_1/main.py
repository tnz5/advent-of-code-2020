# Day 1: Report Repair

def parse_input():
    with open("input.txt", "r") as f:
        input = f.readlines()
        nums = [int(x.strip()) for x in input]
        return nums


def find_product_two(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == 2020:
                return nums[i]*nums[j]


def find_product_three(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(i+2, len(nums)):
                 if nums[i] + nums[j] + nums[k] == 2020:
                     return nums[i]*nums[j]*nums[k]


def main():
    input = parse_input()
    product_two = find_product_two(input)
    print(f"Product of two numbers = {product_two}")
    product_three = find_product_three(input)
    print(f"Product of three numbers= {product_three}")


if __name__ == '__main__':
    main()
