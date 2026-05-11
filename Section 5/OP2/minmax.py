# Test with __Name__
import math
def minmax(max, *args):
    res = args[0]
    for arg in args[1:]:
       if test(arg,res):
        res = arg
    return res


def test(a,b):
    return a > b
if __name__ == "__main__":
    print(minmax(5, 1, 2, 3, 4, 5))
    print(minmax(5, 1, 2, 3, 4, 5, 6))
    print(minmax(5, 10, 20, 30, 40, 50))
def test(a,b):
    return a < b
if __name__ == "__main__":
    print(minmax(5, 1, 2, 3, 4, 5))
    print(minmax(5, 1, 2, 3, 4, 5, 6))
    print(minmax(5, 10, 20, 30, 40, 50))

a =3
b =2
c =4
d =math.fma(a,b,c)
print(d)

