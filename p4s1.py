# -*- encoding: utf-8 -*-


def get_number():
    max_n = 0
    for i in range(999, 1, -1):
        for j in range(999, 1, -1):
            n = i * j
            n_s = str(n)
            if n_s == n_s[::-1] and n > max_n:
                max_n = n
    return max_n

print(get_number())


