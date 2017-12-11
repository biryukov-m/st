for i in range(1, 10):
    # print(i//2)
    if i % 2 != 0:
        print(i, end=' >>> ')
        print(i//2)
    elif i % 2 == 0:
        print(i, end=' >>> ')
        # i += 1
        print((i//2)-1, i//2)

    print()
