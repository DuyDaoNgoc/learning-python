from turtle import forward


NUMBER_OF_DISKS = int(input("Nhập số đĩa: "))
number_of_moves = 2 ** NUMBER_OF_DISKS - 1
rods = {
    'A': list(range(NUMBER_OF_DISKS, 0, -1)),
    'B': [],
    'C': []
}
if 1 <= NUMBER_OF_DISKS <=10:
    def make_allowed_move(rod1, rod2):
        forward = False
        if not rods[rod2]:
            forward = True
        elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
            forward = True
        if forward:
            print(f'Moving disk {rods[rod1][-1]} from {rod1} to {rod2}')
            rods[rod2].append(rods[rod1].pop())
        else:
            print(f'Moving disk {rods[rod2][-1]} from {rod2} to {rod1}')
            rods[rod1].append(rods[rod2].pop())

        # display our progress
        print(rods, '\n')

    def move(n, source, auxiliary, target):
        # display starting configuration
        print(rods, '\n')
        for i in range(number_of_moves):
            remainder = (i + 1) % 3
            if remainder == 1:
                if n % 2 != 0:
                    print(f'Move {i + 1} allowed between {source} and {target}')
                    make_allowed_move(source, target)
                else:
                    print(f'Move {i + 1} allowed between {source} and {auxiliary}')
                    make_allowed_move(source, auxiliary)
            elif remainder == 2:
                if n % 2 != 0:
                    print(f'Move {i + 1} allowed between {source} and {auxiliary}')
                    make_allowed_move(source, auxiliary)
                else:
                    print(f'Move {i + 1} allowed between {source} and {target}')
                    make_allowed_move(source, target)
            elif remainder == 0:
                print(f'Move {i + 1} allowed between {auxiliary} and {target}')
                make_allowed_move(auxiliary, target)

# initiate call from source A to target C with auxiliary B
    move(NUMBER_OF_DISKS, 'A', input('nhập cột phụ: '), input('nhập cột đích: '))
else:
    print(f'Số đĩa quá lớn hoặc không hợp lệ, cần ít nhất {number_of_moves} bước để giải quyết vấn đề')
