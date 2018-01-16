import csv
import urllib.request
def part1():
    try:
        infile = open('book.txt','r')
        outfile = open('myBook.txt','w')
        for line in infile:
            outfile.write(line)
        infile.close()
        outfile.close()
    except FileNotFoundError:
        print('File not found')
def part2():
    try:
        infile = open('planets.csv','r')
        with open('myPlanets.csv','w',newline='') as file:
            header = infile.readline()
            header2 = header.split(',')
            writer = csv.writer(file)
            writer.writerow(header2)
            for line in infile:
                a = line.split(',')
                a[10] = int(a[10]) + 2
                writer.writerow(a)
        infile.close()
    except FileNotFoundError:
        print('File not found')
def part3():
    with urllib.request.urlopen('http://www.cpp.edu/~xjia/VISSIM/Centracs_SynchroTest/PHASING.CSV') as f:
        print(f.read().decode('utf-8'))
part1()
part2()
part3()
