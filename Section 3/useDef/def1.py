

def Fetcher(item, count):

    print(f"Fetching {item} with {count}")
food = str(input("Enter food: "))
def catcher():
    try:
        Fetcher(food,5)
    except IndexError:
        print("Got exception")
    print("Done")
catcher()

L , S = [] , "text"
def modder():
        L.append("added")
        global S ; S = "change"
        Fetcher(food,5)
try:
    modder()
except IndexError:
    print("Got exception")


def Hop():
    a = 1
    b =2
    try:
        print(a/b)
    except ZeroDivisionError:
        print("Cannot divide by zero")
Hop()


import sys
def system_info():
    try:
        print(f"Python version: {sys.version}")
        print(f"Platform: {sys.platform}")
    except Exception as e:
        print(f"An error occurred: {e}")
system_info()



for i in range(10):
    print(f"Processing item {"🦴" * (i+1)}")

for a in range(1):
    for b in range(2):
        for c in range(5):
            print(f"tính {"🦴" * (a+1) , "🦴" * (b+1) , "🤍" * (c + 1)} ")

def attack(atk):
    atk = 8
    if atk <5:
        raise ValueError("Attack value too low")
    print("Attack successful")

try:
    attack(3)
except ValueError as e:
    print(f"Error: {e}")


def GoPlayer(name,lever):

    if lever < 1000:
        raise ValueError("Điểm elo thấp")
    print(f"Player {name} has reached lever {lever}")
try:
    GoPlayer(name = input("nhập tên: "), lever = int(input("nhập điểm elo: ")))
except ValueError as e:
    print(f"Error: {e}")

