def part1():
    L1 = [1,2,3,4,5] ; L2 = [2,3,4,5,1,0]
    print(L1<L2)
    print(L1 != L2)
    L3 = ['1','2','3','4','5']
    #print(  L1>L3) results in error. Cant compare string and int
    print(L1 and L2)
    print(not L3)
    print(not[])
    L1 = [1,2];L2 = [1,2]; L3 = L1
    print(L1 is L2)
    print(L1 is L3)
    sentence = "Hello, Welcome to Python"
    print("Python" in sentence)
    print(min("Python"))
    seasons = ['Summer','Spring','Fall','Winter']
    print(list(enumerate(seasons,start = 1)))
def makeDict(names,scores):
    return dict(zip(names,scores))
def part3():
    names = ['joe','tom','barb','sue','sally']
    scores = [10,17,20,18,15]
    ages = [20,17,19,18,22]
    setTuple = tuple(zip(names,scores))
    fset = frozenset(zip(names,ages))
    print(fset.intersection(setTuple))
def scoreDict(names,scores):
    temp = makeDict(names,scores)
    temp['john'] = 19
    temp['sue'] = 20
    temp['sally'] = 19
    del temp['tom']
    for k,v in temp.items():
        print(k,v)
    return temp
def getMedianScore(temp):
    t = []
    for k,v in temp.items():
        t.append(v)
    print(t[int(len(t)/2)])
class Error(Exception):
    pass
def getScore(name, d):
    returnV = -1
    if name in d:
        returnV = int(d[name])
    if name not in d:
        print(name,' not found')
        raise Error
    return returnV
