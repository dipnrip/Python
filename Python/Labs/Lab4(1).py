'''
#1. module and scripting (tested on login.cpp.edu)

#Once it saved as fibo.py fibo now is the module name.
#Q1: write code to import this module and call the functions.
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=" ")
        a, b = b, a+b
    print()
def fib2(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

#This is for your information only, No question provided. 
#save as fibo_test.py or any other file, may run as $python3 fibo 50 30
#! /usr/bin/env python3
import sys
from fibo import fib, fib2

if __name__ == '__main__' :
    n = int(sys.argv[1])
    print("Fibonacci numbers up to ", n)
    fib(n)
    m = int(sys.argv[2])
    print("Fibonacci numbers up to ",  m,  " in a list")
    print(fib2(m))


#2. time vs. timeit modules, Python program performance
#Q2: Which one is more accurate? time or timeit? Why?

#save as performanceEval.py or any other file name
import time, timeit
import math
 
def doSth (n) :
    total = 0
    for i in range (n) :
        if i % 17 == 0 :
            total = total + math.sqrt(i) - math.sin(i)
    return total

t0 = time.time()
doSth(5000000)
t1 = time.time()
print("Execution time measured by is: ", t1 - t0, " seconds")

print("Execution time measured by timeit ", end=" ")
print(timeit.timeit("lambda x: doSth(x), 5000000"))


#3: calendar module
#Q3: #why we put SUNDAY below? What if we change it to MONDAY?

import calendar
c = calendar.TextCalendar(calendar.SUNDAY)  
c.prmonth(2017, 10)
print (calendar.TextCalendar(calendar.SUNDAY).formatyear(2018, 2, 1, 1, 2))



#turtle modules for drawing
#Q4: Revise the code so that it draws a pentagon. How may degrees should rotate?
#Also, you may use for loop instead of repeatedly coding the line draws.
import turtle

silly = turtle.Turtle()

silly.forward(50)
silly.right(90)     # Rotate clockwise by 90 degrees

silly.forward(50)
silly.right(90)

silly.forward(50)
silly.right(90)

silly.forward(50)
silly.right(90)

turtle.done()


#More drawing fun
#Q5: add painter.speed(5) or any other number to slow down the drawing.
import turtle 

painter = turtle.Turtle()

painter.pencolor("blue")

for i in range(50):
    painter.forward(50)
    painter.left(123) # Let's go counterclockwise this time 
    
painter.pencolor("red")
for i in range(50):
    painter.forward(100)
    painter.left(123)
    
turtle.done()

#Note: you need to install sympy module, try it on your own compputer.
from sympy import *

f = simplify("x ** 2 * x")
print(f)

g = expand("(x - 1) * (x + 1)")
print(g)

roots = solve ("x**2 - 6*x + 8")
print(roots)

answer = solve ("sin(x) - cos(x)")
print(answer)

plot("x**3-x**2+2x-5")

#drawing bargraph, you have to install matplotlib, try it on your own computer.
# -*- coding: utf-8 -
from matplotlib import pyplot
pyplot.bar ([1,2,3,4,5], [1.1, 10.0, 25.4, 55.3, 61])
pyplot.xlabel("month")
pyplot.ylabel("temp")
pyplot.show()
'''
    

