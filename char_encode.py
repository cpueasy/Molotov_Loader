import random
#random = random.SystemRandom()
inputs = input("Enter single line python: ")
def decode(_ll111, _lll11):
    return ''.join([chr((ord(__l11111) ^ ord(__111111))) for (__l11111, __111111) in zip(_ll111, _lll11)])

def encode(str):
    s1 = ""
    s2 = ""
    for p in str:
        e = ord(p)
        t = random.randint(1, 255)
        e = e ^ t
        s1 += chr(e)
        s2 += chr(t)
    return (s1, s2)

encoded = ("exec(''.join([chr((ord(__l11111) ^ ord(__111111))) for (__l11111, __111111) in zip" + str(encode(inputs)) + "]))")
print(encoded)
#print(decode(*encode(inputs)))
