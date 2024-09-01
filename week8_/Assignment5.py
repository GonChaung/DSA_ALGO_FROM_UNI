for i in range(1, 10):
    for j in range(1, 10):
        if 1 < i < 9 and 1 < j < 9:
            print('--', end=' ')
        else:
            print(f'{i*j:2d}', end=' ')
    print()
print()

for i in range (1,10):
    for j in range(1,10):
        if i == 2 and  1 < j < 9:
            print(f'--',end =' ')
        elif 2 < i < 8 and j == 2:
            print(f'--',end=' ')
        elif 2 < i < 8 and j == 8:
            print(f'--',end=' ')
        elif i == 8 and 1 < j < 9:
            print(f'--',end=' ')
        elif 3 < i < 7 and 3 < j < 7:
            print(f'--',end=' ')
        else:
            print(f'{i*j:2d}',end=' ')
    print()
