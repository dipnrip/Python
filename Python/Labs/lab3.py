def part1():
    counter = 0
    maxInt = 0
    lowInt = 0
    a = []
    while True:
        storage = input("Enter numbers: ")
        if int(storage) < 1:
            break
        a.append(int(storage))
        counter += 1
    for i in a:
        if maxInt < i:
            maxInt = i
    lowInt = maxInt
    for i in a:
        if i < lowInt:
            lowInt = i
    print("Max int: ",maxInt)
    print("Min int: ",lowInt)
    print("Number of input: ",counter)
def part2(itemName, taxRate, *purchases):
    total = 0
    for i in purchases:
        total += int(i)
    subTotal = total * ((taxRate/100) + 1)
    print("Item name: ",itemName, " Tax rate: ", taxRate,"%", "Total: {0:.2f}".format(subTotal))
def main():
    part1()
    part2("Fruits", 8, 10, 44 )
    part2("Furniture",10.5,950)
    part2("Toys",7.5,12,5.5,6.5,7.5,9.0)
main()
'''
================= RESTART: /Users/cptnbread/Desktop/lab3.py =================
Enter numbers: 9
Enter numbers: 4
Enter numbers: 2
Enter numbers: 4
Enter numbers: 100
Enter numbers: -4
Max int:  100
Min int:  2
Number of input:  5
Item name:  Fruits  Tax rate:  8 % Total: 58.32
Item name:  Furniture  Tax rate:  10.5 % Total: 1049.75
Item name:  Toys  Tax rate:  7.5 % Total: 41.92
>>> 
'''
