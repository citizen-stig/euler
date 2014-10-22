#!/usr/bin/env python
# -*- encoding: utf-8 -*-

res = 2

prevprev = 1
prev = 2
value = 0

while value <= 4000000:
    value = prevprev + prev
    print(value)
    prevprev = prev
    prev = value
    if value % 2 == 0:
        res += value

print('---------------')
print(res)