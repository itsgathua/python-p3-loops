#!/usr/bin/env python3

def happy_new_year():
    counter = 10
    while counter > 0:
        print(counter)
        counter -= 1
    print("Happy New Year!")

def square_integers(int_list):
    squared_list = []
    for int in int_list:
        int_list = int ** 2
        squared_list.append(int_list)
    return squared_list

def fizzbuzz():
        counter = 1
        while counter < 101:
            if counter % 3 == 0 and counter % 5 == 0:
                print ("FizzBuzz")
            elif counter % 3 == 0:
                print ("Fizz")
            elif counter % 5 == 0:
                print ("Buzz")
            else:
                print (counter)
            counter += 1