import math


characters = [
    # lowercase characters
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    # uppercase characters
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    # space and symbols
    ' ',',','.','?','!','@','#','$','&','*','(',')'
]

# use this method to encode an alphabet character into a binary string
def encode(character):
    charIndex = characters.index(character)
    return '{0:06b}'.format(charIndex)

# use this method to decode a binary string into an alphabet character
def decode(binary):
    charIndex = int(binary, 2)
    return characters[charIndex]


def XOR(bit1, bit2):
    if bit1 == bit2:
        return '0'
    if bit1 != bit2:
        return '1'


def XORonByte(byte, key):
    emsg = ""
    
    for i in range(len(byte)):
        emsg = emsg + XOR(byte[i], key[i])

    return emsg


def XORonLetter(letter, keyLetter):
    letterBinary = encode(letter)
    keyletterBinary = encode(keyLetter)

    encryptedLetter = XORonByte(letterBinary, keyletterBinary)
    return decode(encryptedLetter)


def XORonSentence(sentence, key):
    encryptedSentence = ""
    genKey = generateKey(sentence, key)

    for i in range(len(sentence)):
        encryptedSentence = encryptedSentence + XORonLetter(sentence[i], genKey[i])

    return encryptedSentence


def generateKey(message, key):
    if len(message) == len(key):
        return key
    
    elif len(message) < len(key):
        return key[0:len(message)]

    else:
        genKey = ""

        reps = int(math.floor(len(message)/len(key)))
        remainder = len(message) % len(key)

        genKey = key * reps
        
        remainderKey = key[0:remainder]
        genKey = genKey + remainderKey
        return genKey



msg = input("Please enter a message that you want to en/de-crypt: ")
key = input("Please enter a key: ")

print("Your encrypted message is: ", XORonSentence(msg, key))
