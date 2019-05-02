#!/usr/bin/env python


def diagonalDifference(a):
    c = sum(a[i][i] for i in range(n))
    r = sum(a[i][n - i - 1] for i in range(n))
    return abs(c - r)


if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
        a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
        a.append(a_t)
    result = diagonalDifference(a)
    print(result)
