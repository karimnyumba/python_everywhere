import math
Wall_Height = int(input("Please enter the Wall Height in meters(m): "))
Wall_Width = int(input("Please enter the wWall Width in meters(m): "))


def num_of_cans(Height, Width):
    coverage_per_can = 5
    required_cans = math.ceil((Height * Width) / coverage_per_can)
    print(
        f"The number of cans required to paint a wall with height of {Wall_Height} and width of {Wall_Width} is {required_cans}")


num_of_cans(Wall_Height, Wall_Width)
