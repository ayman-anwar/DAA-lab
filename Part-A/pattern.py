num_rows = 3
for i in range (0, num_rows):
    for j in range(0, i + 1):
        print("* ", end='')
    print()
for i in range (num_rows, 0, -1):
    for j in range(0, i -1):
        print("* ", end='')
    print()
