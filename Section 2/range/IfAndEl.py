from unittest import case

import match

def match(value):
    return value == 3
found = False
x  = [1, 2, 3, 4, 5]
while x and not found:
    if match(x[0]):
        print("Found:", x[0])
        found = True
    else: x = x[1:]
    if not found:
        print("Not found")

OP = input("Enter operation (add, subtract): ")
match OP:
    case "add":
        print("Adding")
    case "subtract":
        print("Subtracting")
    case _:
        print("Unknown operation")



option = input("Enter option (A, B, C): ")
def match_option(option):
    title = "con gì ăn cỏ có 4 chân"
    A = "Con bò"
    B = "Con gà"
    C = "Con lợn"
    result = [A, B, C]
    if title == A:
        if A == "Con bò" and B == "Con gà" and C == "Con lợn":
            match option:
                case "A":
                    print(A)
                case "B":
                    print(B)
                case "C":
                    print(C)
                case _:
                    print("Invalid option")
    else:
        print("Title does not match expected value")


match_option(option)
