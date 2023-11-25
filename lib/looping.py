#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i <= 10 and i > 0:
        print(f"{i}")
        i -= 1
        print("Happy New Year!")   
    pass

def square_integers(int_list):
    # code goes here!
     square_integers = [int*int for int in int_list]
     return square_integers
     pass

def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print (f"{i}") 
    pass
