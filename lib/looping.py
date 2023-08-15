#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    pass
    counter = 10
    while counter >= 1:
        print(counter)
        counter -= 1
        print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    pass
    squared_list = [num ** 2 for num in int_list]
    return squared_list

def fizzbuzz():
    # code goes here!
    pass
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0 :
            print("Buzz")
        else:
            print(number)
