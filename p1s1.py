#!/usr/bin/env python
# -*- encoding: utf-8 -*-


result = sum((x for x in range(1001) if x % 3 == 0 or x % 5 == 0))

print(result)
