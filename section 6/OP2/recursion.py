NUMBER_OF_DISKS = int(input('Nhập số đĩa: '))
rods = {
        'A': list(range(NUMBER_OF_DISKS, 0, -1)),
        'B': [],
        'C': []
    }


if 1 <= NUMBER_OF_DISKS <= 10:

    def move(n, source, auxiliary, target):
        if n > 0:
            # move n - 1 disks from source to auxiliary, so they are out of the way
            move(n - 1, source, target, auxiliary)

            # move the nth disk from source to target
            rods[target].append(rods[source].pop())

            # display our progress
            print(rods, '\n')

            # move the n - 1 disks that we left on auxiliary onto target
            move(n - 1,  auxiliary, source, target)

    # initiate call from source A to target C with auxiliary B
    move(NUMBER_OF_DISKS, 'A', 'B', 'C')
else:
    print("Số đĩa phải nằm trong khoảng từ 1 đến 10.")
    exit()

