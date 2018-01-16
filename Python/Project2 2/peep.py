import turtle as t
def line():
    t.up()
    x = t.xcor()
    t.goto(x+9,0)
    t.down()
    for i in range(2):
        t.left(90)
        t.fd(25)
        t.right(90)
        t.fd(1)
        t.right(90)
        t.fd(25)
        t.left(90)
    t.up()
def dot():
    t.up()
    x = t.xcor()
    t.goto(x+9,0)
    t.down()
    for i in range(2):
        t.left(90)
        t.fd(10)
        t.right(90)
        t.fd(1)
        t.right(90)
        t.fd(10)
        t.left(90)
def draw0():
    line();line();dot();dot();dot()
def draw1():
    dot();dot();dot();line();line()
def draw2():
    dot();dot();line();dot();line()
def draw3():
    dot();dot();line();line();dot()
def draw4():
    dot();line();dot();dot();line()
def draw5():
    dot();line();dot();line();dot()
def draw6():
    dot();line();line();dot();dot()
def draw7():
    line();dot();dot();dot();line()
def draw8():
    line();dot();dot();line();dot()
def draw9():
    line();dot();line();dot();dot()
def start():
    line()
def stop():
    line();
def work(user):
    t.up()
    t.goto(-270,0)
    t.speed(0)
    t.width(1)
    start()
    t.ht()
    for i in range(len(user)):
        if user[i] == "0":
            draw0()
        elif user[i] == '1':
            draw1()
        elif user[i] == '2':
            draw2()
        elif user[i] == '3':
            draw3()
        elif user[i] == '4':
            draw4()
        elif user[i] == '5':
            draw5()
        elif user[i] == '6':
            draw6()
        elif user[i] == '7':
            draw7()
        elif user[i] == '8':
            draw8()
        elif user[i] == '9':
            draw9()
        else:
            continue
    stop()
