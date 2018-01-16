import lab5Functions as f
def main():
    print('*********** 1 ************')
    f.part1()
    names = ['joe','tom','barb','sue','sally']
    scores = [10,17,20,18,15]
    print('*********** 2 ************')
    print(f.makeDict(names,scores))
    print('*********** 3 ************')
    print('Intersection: ',f.part3())
    print('*********** 4 ************')
    print(f.scoreDict(names,scores))
    print('*********** 5 ************')
    f.getMedianScore(f.scoreDict(names,scores))
    print('*********** 6 ************')
    print(getScore('barb',f.makeDict(names,scores)))
    print(getScore('ana',f.makeDict(names,scores)))
main()
    
    
'''
================= RESTART: /Users/cptnbread/Desktop/lab5.py =================
*********** 1 ************
True
True
[2, 3, 4, 5, 1, 0]
False
True
False
True
True
P
[(1, 'Summer'), (2, 'Spring'), (3, 'Fall'), (4, 'Winter')]
*********** 2 ************
{'joe': 10, 'tom': 17, 'barb': 20, 'sue': 18, 'sally': 15}
*********** 3 ************
frozenset({('tom', 17), ('sue', 18)})
Intersection:  None
*********** 4 ************
joe 10
barb 20
sue 20
sally 19
john 19
{'joe': 10, 'barb': 20, 'sue': 20, 'sally': 19, 'john': 19}
*********** 5 ************
joe 10
barb 20
sue 20
sally 19
john 19
20
*********** 6 ************
Traceback (most recent call last):
  File "/Users/cptnbread/Desktop/lab5.py", line 70, in <module>
    main()
  File "/Users/cptnbread/Desktop/lab5.py", line 68, in main
    print(getScore('barb',f.makeDict(names,scores)))
NameError: name 'getScore' is not defined
>>> 
'''
