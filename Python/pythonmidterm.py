l1 = [13, 3, 25, 7, 21, 2, 50, 2, 13, 40, 34, 14, 6, 16]
l2 = [1, -1, 1, 1, -1, 1,-1, 1, 1, -1, 1, -1, 1, -1]
def part1(name,baseFee, *deposits):
    charge = .1
    totalDeposits = sum(deposits)
    if totalDeposits > 20 and totalDeposits < 50:
        charge = .07
    if totalDeposits >= 51:
        charge = .05
    amountCharged = (charge * totalDeposits) + baseFee
    return name, amountCharged
    
def part2(list1, list2):
    if len(list1) != len(list2):
        print('List sizes dont match')
    else:
        newList = []
        for a,b in zip(list1,list2):
            if b == 1:
                newList.append(a)
        if(len(newList) != 0):
            print('Max integer: ',max(newList))
        else:
            print('There are no valid integer to print')
        secondList = list(zip(list1,list2))
        newSortedList = sorted(secondList)
        print(newSortedList)
        for i in range(len(newSortedList)-1,-1,-1):
            if newSortedList[i][1] == -1:
                del newSortedList[i]
        print(newSortedList)
print('Test 1')
print(part1('jack',10,15,29,18,7))
print('Test 2')
print(part1('Joan',10,36))
print('Test 3')
print(part1('David',20,3,5,2,6))
print('Test 4')
print(part1('diana',20))
print('Part 2 Test 1')
part2(l1,l2)
print('Part 2 Test 2')
part2([45,21,4,31,2],[1,1,1,1,1])
print('Part 2 Test 3')
part2([13,3,45],[-1,-1,-1])
    
