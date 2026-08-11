# This program is my own version of the infinite monkey theorum
# It's an interesting problem that explores the theory that, if you gave a monkey a typewriter and infinite time, they would type every possible message in existance.
# This program repeatedly creates 38 character long strings of randomised characters until on of them contains the phrase listed below.
# The program works, however, due to the nature of the problem it has to loop itself a great number of times and can take anywhere between hours and minutes to complete depending on your luck and the speed of your computer.


import random

counter = 1
solved = False
alphabet = " abcdefghijklmnopqrstuvwxyz"
my_phrase = "this is my phrase"

while solved == False:
    result = ""
    for i in range(37):
        result += alphabet[random.randrange(27)]

    if my_phrase in result:
        solved == True
        print("This is the winning result: " + result)
        print("This is how many tries it took: " + counter)
    else :
        counter += counter
    