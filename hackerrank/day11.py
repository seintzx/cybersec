#!/usr/bin/python3


def hourglass(ray):
    c = []
    for i in range(1, 6):
        for j in range(1, 6):
            c.append(
                ray[i - 1][j - 1] + ray[i - 1][j] + ray[i - 1][j + 1] + ray[i]
                [j] + ray[i + 1][j - 1] + ray[i + 1][j] + ray[i + 1][j + 1])
    print(c)


arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)

hourglass(arr)
