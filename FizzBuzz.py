# -*- coding: utf-8 -*-
n = 101
for i in range(1,n):
    if i%3 == 0 and i%5 != 0:
        i = "Fizz"
        print(i)
    elif i%3 != 0 and i%5 == 0:
        i = "Buzz"
        print(i)
    elif i%3 == 0 and i%5 == 0:
        i = "FizzBuzz"
        print(i)
    else:
        print(i)