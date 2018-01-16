import collections as c
from itertools import permutations
alphabet = 'abcdefghijklmnopqrstuvwxyz'
def alphaGen(n):
    temp = c.deque(alphabet)
    temp.rotate(n)
    temp2 = list(temp)
    return ''.join(temp2)
def generateCipher(plainT,n):
    newAlpha = alphaGen(-n)
    keyMap = dict(zip(alphabet,newAlpha))
    return "".join(keyMap.get(i) for i in plainT)
def decipher(plainT,n):
    newAlpha = alphaGen(n)
    keyMap = dict(zip(alphabet,newAlpha))
    return "".join(keyMap.get(i) for i in plainT)
def countFreq(user, freqAlpha):
    temp = {}
    newFreqAlpha = c.Counter(user).most_common()
    index = 0
    for i in newFreqAlpha:
        if i[0] in alphabet:
            temp[freqAlpha[index]] = i[0]
            index += 1
    return temp
def attack(cipher, rounds):
    freqAlpha ='etaoinshrdlcumwfgypbvkjxqz'
    permAlpha = freqAlpha[:4]
    temp = [''.join(p) for p in permutations(permAlpha)]
    for j in range(0,rounds):
        tempAlpha = temp[j] + freqAlpha[4:]
        newAlpha = countFreq(cipher,tempAlpha)
        newAlpha = dict(zip(newAlpha.values(),newAlpha.keys()))
        plainText = ''
        for i in cipher:
            if i in newAlpha.keys():
                plainText += newAlpha[i]
            else:
                plainText += i
        print(plainText)
def main():
    user = input("Enter message: ")
    amount = int(input('Enter shift amount: '))
    plainUser = user.split()
    cipher = ' '.join(generateCipher(i,amount) for i in plainUser)
    rounds = int(input('Number of rounds of frequency analysis: '))
    print('Ciphertext: ',cipher)
    temp1 = cipher.split()
    temp2 = ' '.join(decipher(j,amount) for j in temp1)
    print('back to plain: ',temp2)
    print('Attack attempts')
    attack(cipher, rounds)
main()
