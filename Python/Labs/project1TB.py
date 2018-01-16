def part1(string):
    string2 = string.split()
    acronym = ""
    for i in range (len(string2)):
        if string2[i] == "and" or string2[i] == "of" or string2[i] == "by" or string2[i] == "in" or string2[i] == "on":
            continue
        else:
            temp = string2[i]
            acronym = acronym + temp[:1].capitalize()
    print(acronym)
def part2(num):
    counter = 0
    count = num//2
    while count > 0:
        if num % count == 0:
            counter += count
        count -= 1
    if counter == num:
        print(num," is a perfect number")
    else:
        print(num," is not a perfect number")

def part3(n):
    import random
    import time
    import math
    hit = 0
    currentTime = time.time()
    for i in range(0,n):
        x = random.uniform(0.0,1.0)**2
        y = random.uniform(0.0,1.0)**2
        if math.sqrt(x + y) < 1.0:
            hit += 1
    pi = (float(hit)/n)*4
    timeNow = time.time() - currentTime
    print("Size of n: ",n)
    print("Calculaiton time: ",timeNow)
    print("Approximaiton for pi: ",pi)
def main():
    part1("light amplificaiton by stimulated emission of radiation")
    part1("naitonal aeronautics and space administration")
    part2(6)
    part2(28)
    part2(325)
    part2(496)
    part3(100)
    part3(1000)
    part3(10000)
main()
'''
=============== RESTART: /Users/cptnbread/Desktop/project1.py ===============
LASER
NASA
6  is a perfect number
28  is a perfect number
325  is not a perfect number
496  is a perfect number
Size of n:  100
Calculaiton time:  0.0001819133758544922
Approximaiton for pi:  3.16
Size of n:  1000
Calculaiton time:  0.0011701583862304688
Approximaiton for pi:  3.156
Size of n:  10000
Calculaiton time:  0.012994766235351562
Approximaiton for pi:  3.1464
'''
