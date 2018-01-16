import random as r
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key =      'bpzhgocvjdqswkimlutneryaxf'
def keyGen(alphabet):
   alphabet = list(alphabet)
   r.shuffle(alphabet)
   return ''.join(alphabet)
def defaultKey():
    return key
def substitutionEncrypt(plainText, alphabet, key):
    keyMap = dict(zip(alphabet, key))
    cipherText = ''
    for i in plainText:
        cipherText += keyMap.get(i)
    return cipherText
def work(user, choice):
    if choice == 'R' or choice == 'r':
        randomKey = keyGen(alphabet)
        plainUser = user.split()
        print("Key: ",randomKey)
        for i in plainUser:
           cipher = substitutionEncrypt(i, alphabet, randomKey)
           print(" ", i, " -->" , cipher, end=' ')
    else:
       plainUser = user.split()
       for i in plainUser:
          cipher = substitutionEncrypt(i, alphabet, key)
          print(" ", i, " -->" , cipher, end=' ')
