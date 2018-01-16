defaultKey = ['b','z','h','g','o','c','v','j','d','q','s','w','k','i','m','l','u','t','n','e','r','y','a','x','f']
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def substitutionEncrypt(text, key):
    cipherText = ""
    for c, k in zip(alphabet, defaultKey):
        for i in range(len(text)):
            if text[i] == c
