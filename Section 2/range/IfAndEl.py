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



