# -*- encoding: utf-8 -*-

number = 0

while True:
    number += 19
    for divider in range(1, 21):
        if number % divider != 0:
            break
    else:
        break


print('Answer: {0}'.format(number))
